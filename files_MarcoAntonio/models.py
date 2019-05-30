from sqlalchemy import Column, ForeignKey, Integer, String, Boolean, DateTime, Float, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker, load_only

Base = declarative_base()

class CanaisPorDia(Base):
    __tablename__ = 'canais_geral_por_dia'
    id = Column(Integer, primary_key=True)
    data = Column(Date, nullable=False)
    hora = Column(Integer, nullable=False)
    sucesso = Column(Integer, nullable=False)
    erro_ambiente = Column(Integer, nullable=False)
    erro_negocio = Column(Integer, nullable=False)
    total_transacoes = Column(Integer, nullable=False)
    tempo_medio = Column(Float(16, 8), nullable=False)
