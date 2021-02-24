from datetime import timedelta
from shutil import rmtree

from pytest import fixture

from db_updater.database.connection import Session
from db_updater.importers.data_importer import DataImporter
from db_updater.importers.uls_data_retriever import UlsDataRetriever
from db_updater.utils import get_today_uls


@fixture(params=[True, False])
def retriever(request, external_transaction_session: Session):
    new_test_directory = 'new_test_directory'
    today = get_today_uls()
    yesterday = today - timedelta(days=1)

    try:
        yield UlsDataRetriever(datetime_from=yesterday,
                               datetime_to=today,
                               directory_path=new_test_directory,
                               is_daily=request.param,
                               session=external_transaction_session)
    finally:
        try:
            rmtree(new_test_directory)
        except FileNotFoundError as e:
            pass


@fixture
def data_importer(external_transaction_session: Session):
    return DataImporter(session=external_transaction_session)
