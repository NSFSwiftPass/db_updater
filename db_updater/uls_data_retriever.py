import uuid
from datetime import datetime
from ftplib import FTP
from os import path
from pathlib import Path
from shutil import unpack_archive
from typing import Generator

from db_updater.data_importer import DATA_FILES_DIRECTORY, DataImporter


class UlsDataRetriever:
    ULS_FTP_HOST = 'wirelessftp.fcc.gov'
    DATA_ROOT_DIR = 'pub/uls'
    DATA_COMPLETE_DIR = 'complete'
    DATA_DAILY_DIR = 'daily'

    def __init__(self,
                 complete: bool = False,
                 delete_all_current_entries: bool = False,
                 directory_path: str = DATA_FILES_DIRECTORY,
                 generate_db_classes: bool = False,
                 process_files_after_datetime: datetime = None):
        self.data_importer = DataImporter(generate_db_classes=generate_db_classes,
                                          delete_all_current_entries=delete_all_current_entries,
                                          directory_path=self._make_unique_downloads_folder(directory_path=directory_path))
        today = datetime.now()
        self.process_files_after_datetime = process_files_after_datetime or datetime(year=today.year, month=today.month, day=today.day)

        self.ftp = FTP(self.ULS_FTP_HOST)
        self.ftp.login()
        self.ftp.cwd(f'{self.DATA_ROOT_DIR}/{self.DATA_COMPLETE_DIR if complete else self.DATA_DAILY_DIR}')

    def perform_import_from_uls(self) -> None:
        self._download_from_uls()
        self.data_importer.import_from_directory()

    def _download_from_uls(self) -> None:
        for filename in self._files_after_date():
            filepath = self._download_zip(filename=filename)
            unpack_archive(filepath, path.join(self.data_importer.directory_path))

    def _download_zip(self, filename: str) -> str:
        local_filepath = path.join(self.data_importer.directory_path, filename)
        self.ftp.retrbinary(cmd=f'RETR {filename}',
                            callback=open(local_filepath, 'wb').write)
        return local_filepath

    def _files_after_date(self) -> Generator[str, None, None]:
        for filename in self.ftp.nlst():
            if self._get_day_from_filename(filename) >= self.process_files_after_datetime:
                yield filename

    def _get_day_from_filename(self, filename: str) -> datetime:
        time = self.ftp.voidcmd(f"MDTM {filename}")
        date_str = time.split()[1]
        year = int(date_str[:4])
        month = int(date_str[4:6])
        day = int(date_str[6:8])

        return datetime(year=year, month=month, day=day)

    @staticmethod
    def _make_unique_downloads_folder(directory_path: str) -> str:
        unique_filepath = path.join(directory_path, f'{datetime.now().isoformat()}_{uuid.uuid4().hex}')
        Path(unique_filepath).mkdir(parents=True, exist_ok=True)
        return unique_filepath


if __name__ == '__main__':
    UlsDataRetriever(complete=True, )
