from .meta import DBSession, Base
from sqlalchemy import Column, Integer, String

class Matakuliah(Base):
    __tablename__ = 'matakuliah'
    id = Column(Integer, primary_key=True)
    kode_mk = Column(String(10), unique=True, nullable=False)
    nama_mk = Column(String(100), nullable=False)
    sks = Column(Integer, nullable=False)
    semester = Column(Integer, nullable=False)
