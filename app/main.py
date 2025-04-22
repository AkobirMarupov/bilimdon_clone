from fastapi import FastAPI
from fastapi.openapi.utils import get_openapi

from app.routers import auth
from app.routers import question
from app.routers import submation
from app.routers import participation
from app.routers import options
from app.routers import topics
from app.routers import game
from app.admin.settengs import admin





app = FastAPI()


@app.get("/")
def read_root():
    return {"Asosiy Sahifa Bizda"}


app.include_router(auth.router)
app.include_router(game.router)
app.include_router(question.router)
app.include_router(options.router)
app.include_router(topics.router)
app.include_router(participation.router)
app.include_router(submation.router)



def custom_openapi():
    if app.openapi_schema:
        return app.openapi_schema

    openapi_schema = get_openapi(
        title="Bilimdon Clone API",
        version="0.0.1",
        description="API with JWT-based Authentication",
        routes=app.routes,
    )

    openapi_schema["components"]["securitySchemes"] = {
        "BearerAuth": {
            "type": "http",
            "scheme": "bearer",
            "bearerFormat": "JWT",
        }
    }

    for path in openapi_schema["paths"].values():
        for method in path.values():
            method.setdefault("security", []).append({"BearerAuth": []})

    app.openapi_schema = openapi_schema
    return app.openapi_schema

app.openapi = custom_openapi


# Admin code

admin.mount_to(app=app)


























