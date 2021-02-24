import os
from dataclasses import asdict, dataclass

from db_updater.database.connection import DB_NAME, DB_PASSWORD, DB_URL, DB_USERNAME


@dataclass
class SchemaNames:
    dds_users: str = 'dds_users'
    script_info: str = 'script_info'


def generate_db_classes_file():
    for schema_name in asdict(SchemaNames()).values():
        output_filepath = os.path.join('db_updater', 'database', '../database/classes', f'{schema_name}_classes.py')
        os.system(f'sqlacodegen '
                  f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_NAME} '
                  f'--schema {schema_name} '
                  f'--outfile {output_filepath} ')


if __name__ == '__main__':
    generate_db_classes_file()
