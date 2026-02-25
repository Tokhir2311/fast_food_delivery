from fastapi import FastAPI

from app.routers import auth_router

app = FastAPI(
    title="Foodify delivery service",
    description="Foodify - fast foof delivevery service inspired from Oqtepa and Evos, built in FatsAPI",
)

app.include_router(auth_router)
