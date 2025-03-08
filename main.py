from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import predictions

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return {'message': 'Welcome home'}

app.include_router(predictions.router)