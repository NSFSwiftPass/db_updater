import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

load_dotenv()


DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_URL = os.getenv('DB_URL')
DB_USERNAME = os.getenv('DB_USERNAME')

DB_NAME = 'cu_pass'
SCHEMA_NAME = 'dds_users'


engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}')
Session = sessionmaker(bind=engine)

Base = declarative_base()
