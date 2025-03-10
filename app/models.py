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


    @property
    def day_name(self):
        days = {
            1: "Monday",
            2: "Tuesday",
            3: "Wednesday",
            4: "Thursday",
            5: "Friday",
            6: "Saturday",
            7: "Sunday"
        }
        return days.get(self.coded_day, "Unknown")

    @property
    def zone_name(self):
        zones = {
            50: "Urban City Centers",
            100: "Highways & Expressways",
            150: "Industrial Zones",
            200: "Mountainous Regions"
        }
        return zones.get(self.zone, "Unknown")
