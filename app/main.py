from fastapi import FastAPI
from app.routers.signin import router


app_main = FastAPI()

app_main.include_router(router)

@app_main.get('/')
async def get_root():
    return {"manage": "Asosiy Saxifa"}