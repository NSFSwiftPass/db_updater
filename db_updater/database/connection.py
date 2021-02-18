import os

from dotenv import load_dotenv
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

load_dotenv()


DB_NAME = os.getenv('DB_NAME')
DB_PASSWORD = os.getenv('DB_PASSWORD')
DB_URL = os.getenv('DB_URL')
DB_USERNAME = os.getenv('DB_USERNAME')
SCHEMA_NAME = os.getenv('SCHEMA_NAME')


engine = create_engine(f'postgresql://{DB_USERNAME}:{DB_PASSWORD}@{DB_URL}/{DB_NAME}')
Session = sessionmaker(bind=engine)
