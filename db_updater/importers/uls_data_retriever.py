import logging
import uuid
from datetime import datetime
from ftplib import FTP, error_temp
from os import getenv, path
from pathlib import Path
from re import match
from shutil import unpack_archive
from typing import Generator, List

from retry import retry

from db_updater.database.connection import Session
from db_updater.importers.data_importer import DATA_FILES_DIRECTORY, DataImporter
from db_updater.utils import ULS_TIMEZONE

LOG_LEVEL = getenv('LOG_LEVEL')

logging.basicConfig()
logger = logging.getLogger(__name__)
logger.setLevel(getattr(logging, LOG_LEVEL) if LOG_LEVEL else logging.INFO)


class UlsDataRetriever:
    ULS_FTP_HOST = 'wirelessftp.fcc.gov'
    DATA_ROOT_DIR = 'pub/uls'
    DATA_COMPLETE_DIR = 'complete'
    DATA_DAILY_DIR = 'daily'

    def __init__(self,
                 datetime_from: datetime,
                 datetime_to: datetime,
                 is_daily: bool,
                 directory_path: str = DATA_FILES_DIRECTORY,
                 session: Session = None):
        """

        :param datetime_from: Date threshold after which to retrieve data
        :param datetime_to: Date threshold at the same or before which to retrieve data
        :param is_daily: If true, this will import the daily data file from ULS, and
            otherwise the Sunday complete data files from ULS
        :param directory_path: The directory to house the downloaded data
        """
        self.is_daily = is_daily
        self.session = session or Session()

        self.data_importer = DataImporter(delete_all_current_entries=not self.is_daily,
                                          directory_path=self._make_unique_downloads_folder(directory_path=directory_path),
                                          session=self.session)

        self.datetime_from = datetime_from
        self.datetime_to = datetime_to

        self.ftp = self._connect_ftp()

    def perform_import_from_uls(self) -> None:
        """
        This downloads and imports files one at a time. If downloaded and unpacked all at once, unpacked files with
        the same name will overwrite each other.
        """
        for filename in self._licence_files_after_date():
            logger.debug(f'{datetime.now()}: Downloading {filename}')
            filepath = self._download_zip(filename=filename)

            logger.debug(f'{datetime.now()}: Unpacking {filepath}')
            unpack_archive(filepath, path.join(self.data_importer.directory_path))

            logger.debug(f'{datetime.now()}: Importing...')
            self.data_importer.import_from_directory()
            logger.debug(f'{datetime.now()}: Imported.')

            self._reconnect_ftp_if_timeout()

            [f.unlink() for f in Path(self.data_importer.directory_path).glob("*") if f.is_file()]

        self.session.commit()

    def _connect_ftp(self) -> FTP:
        ftp = FTP(self.ULS_FTP_HOST)
        ftp.login()
        ftp.cwd(f'{self.DATA_ROOT_DIR}/{self.DATA_DAILY_DIR if self.is_daily else self.DATA_COMPLETE_DIR}')
        return ftp

    def _download_from_uls(self) -> None:
        for filename in self._licence_files_after_date():
            filepath = self._download_zip(filename=filename)
            unpack_archive(filepath, path.join(self.data_importer.directory_path))

    def _download_zip(self, filename: str) -> str:
        local_filepath = path.join(self.data_importer.directory_path, filename)
        self.ftp.retrbinary(cmd=f'RETR {filename}',
                            callback=open(local_filepath, 'wb').write)
        return local_filepath

    @property
    def _licence_filenames(self) -> List[str]:
        return [filename for filename in self.ftp.nlst() if match(r'^l_', filename)]

    def _licence_files_after_date(self) -> Generator[str, None, None]:
        for filename in self._licence_filenames:
            if self._get_day_from_filename(filename) >= self.datetime_from:
                yield filename

    def _get_day_from_filename(self, filename: str) -> datetime:
        time = self.ftp.voidcmd(f"MDTM {filename}")
        date_str = time.split()[1]
        year = int(date_str[:4])
        month = int(date_str[4:6])
        day = int(date_str[6:8])

        return ULS_TIMEZONE.localize(datetime(year=year, month=month, day=day))

    @staticmethod
    def _make_unique_downloads_folder(directory_path: str) -> str:
        unique_filepath = path.join(directory_path, f'{datetime.now().isoformat()}_{uuid.uuid4().hex}')
        Path(unique_filepath).mkdir(parents=True, exist_ok=True)
        return unique_filepath

    def _reconnect_ftp_if_timeout(self):
        @retry(error_temp, tries=3, delay=1)
        def check_connection():
            try:
                self.ftp.nlst()
            except error_temp as e:
                self.ftp = self._connect_ftp()
                raise e

        check_connection()


# if __name__ == '__main__':
#     retriever = UlsDataRetriever(datetime_from=ULS_TIMEZONE.localize(datetime(year=2021, month=2, day=20)),
#                                  datetime_to=ULS_TIMEZONE.localize(datetime(year=2021, month=2, day=21)),
#                                  is_daily=True)
#     retriever.perform_import_from_uls()
