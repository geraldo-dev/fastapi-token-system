from fastapi import FastAPI
from app.database import engine, Base

app = FastAPI()


@app.get('/')
def health_check():
    return {"msg": 'bem vindo'}
