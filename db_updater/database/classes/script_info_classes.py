# coding: utf-8
from sqlalchemy import Column, DateTime, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class ScriptInfo(Base):
    __tablename__ = 'script_info'
    __table_args__ = {'schema': 'script_info'}

    script_name = Column(String(50), primary_key=True, nullable=False)
    status = Column(String(20), nullable=False)
    date_from = Column(DateTime(True))
    date_to = Column(DateTime(True))
    timestamp = Column(DateTime(True), primary_key=True, nullable=False)
    error_message = Column(String)
