from fastapi import APIRouter, HTTPException
from .. import schemas, database, models
import pandas as pd
import joblib

router = APIRouter(prefix='/predictions', tags=['Predictions'])

@router.get('', response_model=list[schemas.Prediction])
def get_predictions(db:database.SessionDep):
    predictions = db.query(models.Prediction).all()
    return predictions


@router.get('/{id}', response_model=schemas.Prediction)
def get_prediction(id:int, db:database.SessionDep):
    prediction = db.query(models.Prediction).filter(models.Prediction.id == id).first()
    if not prediction:
        raise HTTPException(status_code=404, detail='Prediction not found.')
    return prediction


@router.post('', status_code=201)
def create_prediction(prediction_data:schemas.PredictionBase, db:database.SessionDep):
    prediction_dict = {'CodedDay': [prediction_data.coded_day], 'Zone': [prediction_data.zone], 'Weather': [prediction_data.zone], 'Temperature': [prediction_data.temperature]}
    df = pd.DataFrame(prediction_dict)
    scaler = joblib.load('standard_scaler.pkl')
    df_scaled = scaler.transform(df.values)
    model = joblib.load('model.pkl')
    prediction = model.predict(df_scaled)
    new_prediction = models.Prediction(**prediction_data.model_dump(), traffic=prediction[0])
    db.add(new_prediction)
    db.commit()
    db.refresh(new_prediction)
    return new_prediction


@router.delete('/{id}')
def delete_prediction(id:int, db:database.SessionDep):
    prediction_query = db.query(models.Prediction).filter(models.Prediction.id == id)
    prediction = prediction_query.first()
    if not prediction:
        raise HTTPException(status_code=404, detail='Prediction not found.')
    prediction_query.delete(synchronize_session=False)
    db.commit()
    return