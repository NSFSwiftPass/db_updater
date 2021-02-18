import uuid
from os.path import isdir, isfile
from re import match
from shutil import rmtree

from db_updater.importers.uls_data_retriever import UlsDataRetriever


def _get_first_filename(retriever: UlsDataRetriever) -> str:
    return retriever.ftp.nlst()[0]


def test_download_zip(retriever: UlsDataRetriever):
    filepath = retriever._download_zip(filename=_get_first_filename(retriever=retriever))
    assert isfile(filepath), 'It should have downloaded the file.'


def test_files_after_date(retriever: UlsDataRetriever):
    for filename in retriever._licence_files_after_date():
        assert retriever._get_day_from_filename(filename) >= retriever.datetime_from,\
            'It should have returned a list of filenames that were modified after the threshold date.'


def test_get_day_from_filename(retriever: UlsDataRetriever):
    date = retriever._get_day_from_filename(_get_first_filename(retriever=retriever))
    assert date, 'It should have returned a date from the filename.'


def test_licence_filenames(retriever: UlsDataRetriever):
    all_filenames = retriever.ftp.nlst()
    assert any(match(r'^a_', filename) for filename in all_filenames), 'It should find some application files in ULS.'
    assert all(match(r'^l_', filename) for filename in retriever._licence_filenames), \
        'It should only find license files in ULS.'


def test_init(retriever: UlsDataRetriever):
    assert retriever.datetime_from, 'It should have set a threshold date.'
    assert retriever.ftp, 'It should have connected to the ULS ftp site.'
    assert retriever.session, 'It should have initialized a DB session.'


def test_make_unique_downloads_folder():
    new_test_directory = f'test_{uuid.uuid4().hex}'
    new_directory = UlsDataRetriever._make_unique_downloads_folder(new_test_directory)
    assert isdir(new_directory), 'It should have created the new directory.'

    try:
        rmtree(new_test_directory)
    except FileNotFoundError as e:
        pass

