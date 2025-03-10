from pydantic import BaseModel

class PredictionBase(BaseModel):
    coded_day:int
    zone:int
    weather:int
    temperature:int

class PredictionCreate(PredictionBase):
    pass

class Prediction(PredictionBase):
    id:int
    traffic: float


class PredictionSchema(BaseModel):
    id: int
    coded_day: int
    day_name: str
    zone: int
    zone_name: str
    weather: int
    temperature: int
    traffic: float

    class Config:
        from_attributes = True