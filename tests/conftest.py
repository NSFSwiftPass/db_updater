from shutil import rmtree

from pytest import fixture

from db_updater.importers.uls_data_retriever import UlsDataRetriever


@fixture
def retriever():
    new_test_directory = 'new_test_directory'

    try:
        yield UlsDataRetriever(directory_path=new_test_directory)
    finally:
        try:
            rmtree(new_test_directory)
        except FileNotFoundError as e:
            pass
