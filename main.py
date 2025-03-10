from fastapi import FastAPI
from app import models
from app.database import engine
from app.routers import predictions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "*",
   
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

models.Base.metadata.create_all(bind=engine)

@app.get('/')
def index():
    return {'message': 'Welcome home'}

app.include_router(predictions.router)