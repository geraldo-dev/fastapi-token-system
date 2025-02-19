from fastapi import FastAPI
from app import routes

app = FastAPI()

app.include_router(routes.router, tags=['users'])
app.include_router(routes.test_router, tags=['test'])


@app.get('/')
def health_check():
    return {"msg": 'bem vindo'}
