from datetime import datetime

from sqlalchemy import Column, Integer, BigInteger, Boolean, String, ForeignKey, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UploadFiles(Base):
    """Модель таблицы тем"""
    __tablename__ = 'upload_files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    upload_name = Column(String)
    path = Column(String)
    user = Column(String)
    active = Column(Boolean)
    datetime = Column(DateTime)

    def __init__(self, name, path, user=None, active=True):
        self.name = name
        self.path = path
        self.user = user
        self.active = active
        self.datetime = datetime.now()

    def __repr__(self):
        return f'<UploadFiles({self.name}, {self.path}, {self.user}, {self.active})>'


class InitDocumentJson(Base):
    """ Таблица с JSON исходного документа """
    __tablename__ = 'init_document_json'

    id = Column(Integer, primary_key=True)
    json = Column(String)

    init_file_id = Column(Integer, ForeignKey('upload_files.id'))

    upload_files = relationship('UploadFiles', uselist=True, cascade='delete,all')


class CurrentDocumentJson(Base):
    """ Таблица с JSON текущей редакции документа """
    __tablename__ = 'current_document_json'

    id = Column(Integer, primary_key=True)
    json = Column(String)

    init_json_id = Column(Integer, ForeignKey('init_document_json.id'))

    init_document_json = relationship('InitDocumentJson', uselist=True, cascade='delete,all')


class DiffJson(Base):
    """ Таблица с JSON изменения документа """
    __tablename__ = 'diff_json'

    id = Column(Integer, primary_key=True)
    json = Column(String)
    datetime = Column(DateTime)

    init_json_id = Column(Integer, ForeignKey('current_document_json.id'))

    current_document_json = relationship('CurrentDocumentJson', uselist=True, cascade='delete,all')