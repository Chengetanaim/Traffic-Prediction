from sqlalchemy import Column, Integer, String, FLOAT
from .database import Base


class Prediction(Base):
    __tablename__ = 'predictions'
    
    id = Column(Integer, primary_key=True, index=True)
    coded_day = Column(Integer, nullable=False)
    zone = Column(Integer, nullable=False)
    weather = Column(Integer, nullable=False)
    temperature = Column(Integer, nullable=False)
    traffic = Column(FLOAT, nullable=False)
