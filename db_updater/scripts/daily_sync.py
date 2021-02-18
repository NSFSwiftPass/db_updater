import uuid
from calendar import SUNDAY
from datetime import datetime, timedelta
from shutil import rmtree
from typing import Optional

from db_updater.database.classes.script_info_classes import ScriptInfo

from db_updater.database.connection import Session
from db_updater.importers.uls_data_retriever import UlsDataRetriever
from db_updater.utils import get_now_uls, get_now_utc, get_today_uls


class DailySyncStatuses:
    begin: str = 'BEGIN'
    error: str = 'ERROR'
    success: str = 'SUCCESS'


class DailySync:
    SCRIPT_NAME = 'daily_dds_sync'

    date_from: Optional[datetime] = None
    date_to: Optional[datetime] = None

    this_script_info: ScriptInfo = None

    def __init__(self):
        three_days_ago = get_now_uls() - timedelta(days=3)

        self.is_daily = get_today_uls().weekday() != SUNDAY
        self.current_run_timestamp = get_now_utc()
        self.session = Session()
        self.date_to = get_now_uls()

        if self.is_daily:
            last_script_info = self._get_last_script_info()
            self.date_from = last_script_info.date_to if last_script_info else three_days_ago
        else:
            self.date_from = get_today_uls()

        self.retriever = UlsDataRetriever(datetime_from=self.date_from,
                                          datetime_to=self.date_to,
                                          is_daily=self.is_daily,
                                          session=self.session)

    def begin(self) -> None:
        self._assert_none_running()
        self._create_script_info_entry()

        try:
            self.retriever.perform_import_from_uls()
            rmtree(self.retriever.data_importer.directory_path, ignore_errors=True)
            self._update_script_info_success()
        except Exception as e:
            self._update_script_info_error(error_message=str(e))
        finally:
            self.session.close()

    def _assert_initial_script_info_entry(self) -> None:
        if not self.this_script_info:
            raise AssertionError('Initial script info entry has not been created.')

    def _assert_none_running(self) -> None:
        if self.session.query(ScriptInfo).filter(ScriptInfo.script_name == self.SCRIPT_NAME,
                                                 ScriptInfo.status == DailySyncStatuses.begin).count():
            raise AssertionError('There is already a sync in progress.')

    def _create_script_info_entry(self) -> None:
        self.this_script_info = ScriptInfo(id=uuid.uuid4().hex,
                                           script_name=self.SCRIPT_NAME,
                                           status=DailySyncStatuses.begin,
                                           date_from=self.date_from,
                                           date_to=self.date_to,
                                           last_updated=self.current_run_timestamp,
                                           timestamp=self.current_run_timestamp)
        self.session.add(self.this_script_info)
        self.session.commit()

    def _get_last_script_info(self) -> Optional[ScriptInfo]:
        return self.session.query(ScriptInfo)\
            .filter(ScriptInfo.script_name == self.SCRIPT_NAME, ScriptInfo.status == DailySyncStatuses.success)\
            .order_by(ScriptInfo.timestamp.desc())\
            .first()

    def _get_uls_data_retriever(self) -> UlsDataRetriever:
        return UlsDataRetriever(datetime_from=self.date_from,
                                datetime_to=self.date_to,
                                is_daily=self.is_daily)

    def _set_last_updated(self) -> None:
        self.this_script_info.last_updated = get_now_utc()

    def _update_script_info_success(self) -> None:
        self._assert_initial_script_info_entry()

        self.this_script_info.status = DailySyncStatuses.success
        self._set_last_updated()
        self.session.commit()

    def _update_script_info_error(self, error_message: str) -> None:
        self._assert_initial_script_info_entry()

        self.this_script_info.status = DailySyncStatuses.error
        self.this_script_info.error_message = error_message
        self._set_last_updated()
        self.session.commit()


if __name__ == '__main__':
    DailySync().begin()
