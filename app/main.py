from fastapi import  FastAPI

from app.routers.auth import router as auth_router
from app.routers.question import router as question_router
from app.routers.options import router as option_router
from app.routers.topics import router as topic_router


app = FastAPI()


def read_root():
    return {"Hello": "World"}


app.include_router(auth_router)
app.include_router(question_router)
app.include_router(option_router)
app.include_router(topic_router)