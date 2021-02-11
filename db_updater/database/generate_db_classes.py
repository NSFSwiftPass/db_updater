import os

from db_updater.connection import DB_NAME, DB_PASSWORD, DB_URL, DB_USERNAME, SCHEMA_NAME

OUTPUT_FILEPATH = os.path.join('db_updater', 'database', 'db_classes.py')


def generate_db_classes_file():
    os.system(f'sqlacodegen '
              f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_NAME} '
              f'--schema {SCHEMA_NAME} '
              f'--outfile {OUTPUT_FILEPATH} ')


if __name__ == '__main__':
    generate_db_classes_file()
