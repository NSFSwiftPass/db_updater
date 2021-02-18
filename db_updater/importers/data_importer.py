import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional

from sqlalchemy import Table
from sqlalchemy.sql import Insert

from db_updater.database.classes import dds_users_classes
from db_updater.database.connection import Session

DATA_FILES_DIRECTORY = os.path.join('db_updater', 'database', 'downloaded_data')
TABLE_VARIABLE_NAME_PREFIX = 't_PUBACC_'


class DataImporter:
    def __init__(self,
                 delete_all_current_entries: bool = False,
                 directory_path: str = DATA_FILES_DIRECTORY,
                 file_extension: str = 'dat',
                 session: Session = None):
        self.delete_all_current_entries = delete_all_current_entries
        self.file_extension = file_extension
        self.directory_path = directory_path

        self.session = session or Session()

    def import_from_directory(self):
        if self.delete_all_current_entries:
            self._delete_all_current_entries()
        self._read_and_import_lines()

    def _convert_entry_values_to_python(self, entry_values: List[str]) -> Dict[str, Any]:
        table = self._find_matching_table(entry_values=entry_values)
        table_columns = table.columns
        headers = table.columns.keys()

        def value_mapper(column_key, entry_value):
            column_info = table_columns[column_key]
            column_type = column_info.type.python_type

            if column_type == datetime:
                return datetime.strptime(entry_value, '%m/%d/%Y') if entry_value else None

            return column_type(entry_value) if entry_value else None

        return {key: value_mapper(key, value) for key, value in zip(headers, entry_values)}

    def _delete_all_current_entries(self):
        all_tables = [value for variable_name, value in dds_users_classes.__dict__.items() if
                      re.match(f'^{TABLE_VARIABLE_NAME_PREFIX}[A-Z]{{2}}', variable_name)]

        for table in all_tables:
            delete_clause = table.delete()
            self.session.execute(delete_clause)

        self.session.flush()

    @staticmethod
    def _find_matching_table(entry_values: List[str]) -> Optional[Table]:
        return getattr(dds_users_classes, f'{TABLE_VARIABLE_NAME_PREFIX}{entry_values[0]}', None)

    def _get_entry_insertion(self, entry_line: str) -> Optional[Insert]:
        entry_values = entry_line.split('|')
        table = self._find_matching_table(entry_values=entry_values)
        if table is None:
            return

        insert_values = self._convert_entry_values_to_python(entry_values)

        return table.insert().values(**insert_values)

    def _get_entry_lines_from_directory(self) -> Generator[str, None, None]:
        for filepath in Path(self.directory_path).glob(f'*.{self.file_extension}'):
            with open(filepath, "r") as file:
                for line in file.readlines():
                    yield line.rstrip()

    def _read_and_import_lines(self):
        for entry_line in self._get_entry_lines_from_directory():
            insert_clause = self._get_entry_insertion(entry_line=entry_line)
            if insert_clause is not None:
                self.session.execute(insert_clause)

        self.session.flush()
