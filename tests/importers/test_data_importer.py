from db_updater.database.classes.dds_users_classes import PUBACCAN
from db_updater.importers.data_importer import DataImporter
from tests.importers.conftest import ARBITRARY_ANTENNA_LINE, ARBITRARY_TABLE_ID_VALID


def test_init():
    data_importer = DataImporter()
    assert data_importer.directory_path, 'It should initialize the directory path.'
    assert len(data_importer.all_tables), 'It should find all dds_users tables.'


def test_delete_all_current_entries(antenna_entry, data_importer):
    antenna_query = data_importer.session.query(PUBACCAN)

    assert antenna_query.count(), 'It should start with an entry.'

    data_importer._delete_all_current_entries()

    assert not antenna_query.count(), 'It should have no entries.'


def test_entry_exists(antenna_entry, data_importer):
    assert data_importer._entry_exists(table=antenna_entry.__table__, entry_values={
        'antenna_number': antenna_entry.antenna_number,
        'location_number': antenna_entry.location_number,
        'unique_system_identifier': antenna_entry.unique_system_identifier
    }), 'It should have found the entry.'


def test_entry_exists_false(antenna_entry, data_importer):
    assert not data_importer._entry_exists(table=antenna_entry.__table__, entry_values={
        'antenna_number': antenna_entry.antenna_number + 1,
        'location_number': antenna_entry.location_number,
        'unique_system_identifier': antenna_entry.unique_system_identifier
    }), 'It should not have found the entry.'


def test_entry_exists_no_primary_key(frequency_coordination_entry, data_importer):
    assert not data_importer._entry_exists(table=frequency_coordination_entry[0], entry_values={
        'coordination_number': frequency_coordination_entry[1].coordination_number,
        'unique_system_identifier': frequency_coordination_entry[1].unique_system_identifier
    }), 'It should not have found the entry.'


def test_find_matching_table(data_importer):
    assert data_importer._find_matching_table([ARBITRARY_TABLE_ID_VALID]) is not None


def test_find_matching_table_nonexistent(data_importer):
    arbitrary_table_id_invalid = 'invalid_table_id'
    assert data_importer._find_matching_table([arbitrary_table_id_invalid]) is None


def test_get_modify_query_insert(data_importer):
    assert 'INSERT' in str(data_importer._get_modify_query(entry_line=ARBITRARY_ANTENNA_LINE)),\
        'It should return an insert query.'


def test_get_modify_query_update(antenna_entry, data_importer):
    assert 'UPDATE' in str(data_importer._get_modify_query(entry_line=ARBITRARY_ANTENNA_LINE)),\
        'It should return an update query.'
