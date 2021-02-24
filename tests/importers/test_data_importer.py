from db_updater.database.classes.dds_users_classes import PUBACCAN
from db_updater.importers.data_importer import DataImporter


ARBITRARY_TABLE_ID_VALID = 'AN'


def test_init():
    data_importer = DataImporter()
    assert data_importer.directory_path, 'It should initialize the directory path.'
    assert len(data_importer.all_tables), 'It should find all dds_users tables.'


def test_delete_all_current_entries(data_importer):
    antenna_entry = PUBACCAN(unique_system_identifier=1,
                             antenna_number=1,
                             location_number=1)
    data_importer.session.add(antenna_entry)

    antenna_query = data_importer.session.query(PUBACCAN)

    assert antenna_query.count(), 'It should start with an entry.'

    data_importer._delete_all_current_entries()

    assert not antenna_query.count(), 'It should have no entries.'


def test_find_matching_table(data_importer):
    assert data_importer._find_matching_table([ARBITRARY_TABLE_ID_VALID]) is not None


def test_find_matching_table_nonexistent(data_importer):
    arbitrary_table_id_invalid = 'invalid_table_id'
    assert data_importer._find_matching_table([arbitrary_table_id_invalid]) is None
