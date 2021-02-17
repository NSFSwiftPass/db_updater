import uuid
from os.path import isdir, isfile
from shutil import rmtree

from db_updater.uls_data_retriever import UlsDataRetriever


def _get_first_filename(retriever: UlsDataRetriever) -> str:
    return retriever.ftp.nlst()[0]


def test_download_zip(retriever: UlsDataRetriever):
    filepath = retriever._download_zip(filename=_get_first_filename(retriever=retriever))
    assert isfile(filepath), 'It should have downloaded the file.'


def test_get_day_from_filename(retriever: UlsDataRetriever):
    date = retriever._get_day_from_filename(_get_first_filename(retriever=retriever))
    assert date, 'It should have returned a date from the filename.'


def test_files_after_date(retriever: UlsDataRetriever):
    for filename in retriever._files_after_date():
        assert retriever._get_day_from_filename(filename) >= retriever.process_files_after_datetime,\
            'It should have returned a list of filenames that were modified after the threshold date.'


def test_init(retriever: UlsDataRetriever):
    assert retriever.process_files_after_datetime, 'It should have set a threshold date.'
    assert retriever.ftp, 'It should have connected to the ULS ftp site.'


def test_make_unique_downloads_folder():
    new_test_directory = f'test_{uuid.uuid4().hex}'
    new_directory = UlsDataRetriever._make_unique_downloads_folder(new_test_directory)
    assert isdir(new_directory), 'It should have created the new directory.'

    try:
        rmtree(new_test_directory)
    except FileNotFoundError as e:
        pass

