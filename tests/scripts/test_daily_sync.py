import uuid
from calendar import MONDAY, SUNDAY
from datetime import timedelta
from functools import partial
from typing import Callable

from pytest_mock import MockerFixture

from db_updater import utils
from db_updater.database.classes.script_info_classes import ScriptInfo
from db_updater.scripts.daily_sync import DailySync, DailySyncStatuses
from db_updater.utils import get_now_uls, get_today_uls


def test_assert_none_running(daily_sync: DailySync):
    assert daily_sync._assert_none_running() is None, 'It should not have asserted that there was a script in progress.'

    daily_sync._create_script_info_entry()
    try:
        daily_sync._assert_none_running()
        assert False, 'It should have asserted that there was a script in progress.'
    except AssertionError as e:
        pass


def test_create_script_info_entry(daily_sync: DailySync):
    daily_sync._create_script_info_entry()

    new_entry_query = daily_sync.session\
        .query(ScriptInfo)\
        .filter(ScriptInfo.script_name == daily_sync.SCRIPT_NAME)
    assert new_entry_query.count() == 1, 'It should have created a new script info entry.'

    refreshed_entry = new_entry_query.first()
    assert refreshed_entry.status == DailySyncStatuses.begin, 'It should have set the status to begin.'

    assert refreshed_entry.last_updated == daily_sync.current_run_timestamp, \
        'It should have initialized the `last_updated` time.'


def test_get_last_script_info(daily_sync: DailySync):
    localized_timestamps = [get_now_uls() - timedelta(days=i) for i in range(3)]

    session = daily_sync.session
    for index, timestamp in enumerate(localized_timestamps):
        script_info = ScriptInfo(id=uuid.uuid4().hex,
                                 script_name=daily_sync.SCRIPT_NAME,
                                 status=DailySyncStatuses.success if index else DailySyncStatuses.error,
                                 timestamp=timestamp)
        session.add(script_info)

    session.commit()

    num_entries_in_db = session\
        .query(ScriptInfo)\
        .filter(ScriptInfo.script_name == daily_sync.SCRIPT_NAME)\
        .count()
    assert num_entries_in_db == len(localized_timestamps), 'It should have set up the correct number of test entries.'

    latest_run = daily_sync._get_last_script_info()
    assert latest_run.timestamp == localized_timestamps[1], 'It should have retrieved the newest successful entry.'


def test_get_last_script_info_none(daily_sync: DailySync):
    assert daily_sync._get_last_script_info() is None, 'It should have retrieved no latest run.'


def test_init():
    daily_sync = DailySync()
    assert daily_sync.current_run_timestamp, 'It should have created a current run timestamp.'
    assert daily_sync.date_to, 'It should have created a `date_to` timestamp.'
    assert daily_sync.retriever, 'It should have created a ULS data retriever.'
    assert daily_sync.session, 'It should have created a session.'


def test_init_sunday(mocker: MockerFixture):
    localize_mock = mocker.patch.object(utils.ULS_TIMEZONE, 'localize')
    localize_mock.return_value.weekday.return_value = SUNDAY

    daily_sync = DailySync()
    assert not daily_sync.is_daily, 'It should have set this to be a weekly run.'
    assert daily_sync.date_from == get_today_uls(), 'It should have set the date to the beginning of today.'


def test_init_other_day(mocker: MockerFixture):
    localize_mock = mocker.patch.object(utils.ULS_TIMEZONE, 'localize')
    localize_mock.return_value.weekday.return_value = MONDAY

    daily_sync = DailySync()
    assert daily_sync.is_daily, 'It should have set this to be a daily run.'
    assert daily_sync.date_from, 'It should have set the date from.'
    assert daily_sync.date_to, 'It should have set the date to.'
    assert daily_sync.date_from <= daily_sync.date_to, 'It should have set the date from to be before the date to.'


def test_update_script_info_success(daily_sync: DailySync):
    daily_sync._create_script_info_entry()
    daily_sync._update_script_info_success()

    refreshed_entry = daily_sync._get_last_script_info()
    assert refreshed_entry.status == DailySyncStatuses.success, \
        'It should have updated the status successful.'

    _assert_last_updated_greater_than(daily_sync=daily_sync, refreshed_entry=refreshed_entry)


def test_update_script_info_error(daily_sync: DailySync):
    error_message = 'error_message'
    daily_sync._create_script_info_entry()
    daily_sync._update_script_info_error(error_message=error_message)

    refreshed_entry = daily_sync.session.query(ScriptInfo).get((daily_sync.SCRIPT_NAME, daily_sync.current_run_timestamp))
    assert refreshed_entry.status == DailySyncStatuses.error, \
        'It should have updated the status to have an error.'

    assert refreshed_entry.error_message == error_message, \
        'It should have updated the status to have an error message.'

    _assert_last_updated_greater_than(daily_sync=daily_sync, refreshed_entry=refreshed_entry)


def test_update_script_info_success_no_initial(daily_sync: DailySync):
    _assert_update_script_infos_no_initial(daily_sync._update_script_info_success)


def test_update_script_info_error_no_initial(daily_sync: DailySync):
    error_func = partial(daily_sync._update_script_info_error, error_message='error_message')
    _assert_update_script_infos_no_initial(error_func)


def _assert_update_script_infos_no_initial(func: Callable[[], None]):
    try:
        func()
        assert False, 'It should not have attempted to update the entry with no initial entry.'
    except AssertionError as e:
        pass


def _assert_last_updated_greater_than(daily_sync: DailySync, refreshed_entry: ScriptInfo):
    assert refreshed_entry.last_updated > daily_sync.current_run_timestamp, \
        'It should have updated `last_updated` time.'
