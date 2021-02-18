import os

from db_updater.database.connection import DB_NAME, DB_PASSWORD, DB_URL, DB_USERNAME, SCHEMA_NAME


def generate_db_classes_file():
    output_filepath = os.path.join('db_updater', 'database', '../database/classes', f'{SCHEMA_NAME}_classes.py')
    os.system(f'sqlacodegen '
              f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_NAME} '
              f'--schema {SCHEMA_NAME} '
              f'--outfile {output_filepath} ')


if __name__ == '__main__':
    generate_db_classes_file()
