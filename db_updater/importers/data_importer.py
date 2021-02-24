import os
import re
from datetime import datetime
from pathlib import Path
from typing import Any, Dict, Generator, List, Optional, Tuple

from sqlalchemy import Table
from sqlalchemy.orm import Query

from db_updater.database.classes import dds_users_classes
from db_updater.database.connection import Session

DATA_FILES_DIRECTORY = os.path.join('db_updater', 'database', 'downloaded_data')
CLASS_VARIABLE_NAME_PREFIX = 'PUBACC'
TABLE_VARIABLE_NAME_PREFIX = f't_{CLASS_VARIABLE_NAME_PREFIX}_'


class DataImporter:
    def __init__(self,
                 delete_all_current_entries: bool = False,
                 directory_path: str = DATA_FILES_DIRECTORY,
                 file_extension: str = 'dat',
                 session: Session = None):
        self.file_extension = file_extension
        self.directory_path = directory_path

        self.all_tables = self._get_all_tables()

        self.session = session or Session()

        if delete_all_current_entries:
            self._delete_all_current_entries()

    def import_from_directory(self):
        for entry_line in self._get_entry_lines_from_directory():
            query = self._get_modify_query(entry_line)
            if query is not None:
                self.session.execute(query)

        self.session.flush()

    def _convert_entry_values_to_python(self, entry_values: List[str]) -> Dict[str, Any]:
        table = self._find_matching_table(entry_values=entry_values)
        table_columns = table.columns
        headers = table.columns.keys()

        self._pad_entry_values(entry_values=entry_values, headers=headers)

        def value_mapper(column_key, entry_value):
            column_info = table_columns[column_key]
            column_type = column_info.type.python_type

            if column_type == datetime:
                return datetime.strptime(entry_value, '%m/%d/%Y') if entry_value else None

            return column_type(entry_value) if entry_value else None

        return {key: value_mapper(key, value) for key, value in zip(headers, entry_values)}

    def _delete_all_current_entries(self) -> None:
        for table in self.all_tables.values():
            delete_clause = table.delete()
            self.session.execute(delete_clause)

        self.session.flush()

    def _entry_exists(self, table: Table, entry_values: Dict[str, Any]) -> bool:
        primary_key = table.primary_key
        if not len(primary_key):
            return False

        select_query = self._match_primary_key(table=table, entry_values=entry_values, initial_query=table.select())

        return bool(self.session.execute(select_query).rowcount)

    def _find_matching_table(self, entry_values: List[str]) -> Optional[Table]:
        table_id = entry_values[0]
        return self.all_tables.get(table_id, None)

    @staticmethod
    def _get_all_tables() -> Dict[str, Table]:
        return {variable_name[-2:]: getattr(table_or_class, '__table__', table_or_class)
                for variable_name, table_or_class in dds_users_classes.__dict__.items()
                if re.match(f'^({CLASS_VARIABLE_NAME_PREFIX}|{TABLE_VARIABLE_NAME_PREFIX})[A-Z]{{2}}', variable_name)}

    def _get_entry_values(self, entry_line: str) -> Optional[Tuple[Table, Dict[str, Any]]]:
        """
        :param entry_line: The incoming line from ULS
        :return: a tuple with the table to insert into and the dict element to be inserted
        """
        entry_values = entry_line.split('|')
        table = self._find_matching_table(entry_values=entry_values)
        if table is None:
            return

        return table, self._convert_entry_values_to_python(entry_values)

    def _get_entry_lines_from_directory(self) -> Generator[str, None, None]:
        for filepath in Path(self.directory_path).glob(f'*.{self.file_extension}'):
            with open(filepath, "r") as file:
                for line in file.readlines():
                    yield line.rstrip()

    def _get_modify_query(self, entry_line: str) -> Optional[Query]:
        entry_values_with_table = self._get_entry_values(entry_line=entry_line)
        if not entry_values_with_table:
            return None

        table, entry_values = entry_values_with_table
        if self._entry_exists(table=table, entry_values=entry_values):
            update_query = self._match_primary_key(table=table, entry_values=entry_values,
                                                   initial_query=table.update())
            return update_query.values(entry_values)
        else:
            return table.insert().values(entry_values)

    @staticmethod
    def _match_primary_key(table: Table, entry_values: Dict[str, Any], initial_query: Query) -> Query:
        for column in table.primary_key.columns.keys():
            initial_query = initial_query.where(table.columns[column] == entry_values[column])
        return initial_query

    @staticmethod
    def _pad_entry_values(entry_values: List[str], headers: List[str]) -> None:
        """
        Entry values do not always match the length of the headers. Pad with empty values.
        """
        for i in range(len(headers) - len(entry_values)):
            entry_values.append('')


# if __name__ == '__main__':
#     data_importer = DataImporter(delete_all_current_entries=True,
#                                  file_extension='txt')
#     data_importer.import_from_directory()
#     data_importer.session.commit()
