from datetime import timedelta
from shutil import rmtree
from typing import Tuple

from pytest import fixture
from sqlalchemy import Table
from sqlalchemy.engine import RowProxy

from db_updater.database.classes.dds_users_classes import PUBACCAN, t_PUBACC_FC
from db_updater.database.connection import Session
from db_updater.importers.data_importer import DataImporter
from db_updater.importers.uls_data_retriever import UlsDataRetriever
from db_updater.utils import get_today_uls
from tests.confest import external_transaction_session


ARBITRARY_TABLE_ID_VALID = 'AN'
ARBITRARY_ANTENNA_LINE = 'AN|1|||WPUF387||1|1||T||0.9|Andrew|PL6-65|-0.2|H|1.7|39.9|142.4|||||||||||Boulder|||1|||||'
ARBITRARY_ANTENNA_LINE_ARR = ARBITRARY_ANTENNA_LINE.split('|')


@fixture
def antenna_entry(data_importer) -> PUBACCAN:
    antenna_entry = PUBACCAN(unique_system_identifier=int(ARBITRARY_ANTENNA_LINE_ARR[1]),
                             antenna_number=int(ARBITRARY_ANTENNA_LINE_ARR[6]),
                             location_number=int(ARBITRARY_ANTENNA_LINE_ARR[7]))
    data_importer.session.add(antenna_entry)
    data_importer.session.flush()

    return antenna_entry


@fixture
def data_importer(external_transaction_session: Session) -> DataImporter:
    return DataImporter(session=external_transaction_session)


@fixture
def frequency_coordination_entry(data_importer) -> Tuple[Table, RowProxy]:
    entry_values = {
        'unique_system_identifier': 1,
        'coordination_number': 1
    }
    insert_clause = t_PUBACC_FC.insert().values(entry_values)
    data_importer.session.execute(insert_clause)
    data_importer.session.flush()

    inserted_entry = list(data_importer.session.execute(t_PUBACC_FC.select().where(t_PUBACC_FC.c.unique_system_identifier == 1)))[0]
    return t_PUBACC_FC, inserted_entry


@fixture(params=[True, False])
def retriever(request, external_transaction_session: Session) -> UlsDataRetriever:
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

