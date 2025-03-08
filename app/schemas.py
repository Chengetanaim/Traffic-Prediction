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