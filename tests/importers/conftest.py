from datetime import timedelta
from shutil import rmtree

from pytest import fixture

from db_updater.importers.uls_data_retriever import UlsDataRetriever
from db_updater.utils import get_today_uls


@fixture
def retriever():
    new_test_directory = 'new_test_directory'
    today = get_today_uls()
    yesterday = today - timedelta(days=1)

    try:
        yield UlsDataRetriever(datetime_from=yesterday,
                               datetime_to=today,
                               directory_path=new_test_directory,
                               is_daily=True)
    finally:
        try:
            rmtree(new_test_directory)
        except FileNotFoundError as e:
            pass
