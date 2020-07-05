from sqlalchemy import Column, Integer, BigInteger, Boolean, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()

class UploadFiles(Base):
    """Модель таблицы тем"""
    __tablename__ = 'upload_files'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    path = Column(String)
    user = Column(String)
    active = Column(Boolean)

    def __init__(self, name, path, user=None, active=True):
        self.name = name
        self.path = path
        self.user = user
        self.active = active

    def __repr__(self):
        return f'<UploadFiles({self.name}, {self.path}, {self.user}, {self.active})>'
