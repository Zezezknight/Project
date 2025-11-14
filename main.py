from __future__ import annotations

from fastapi import FastAPI

from database import mongo_database

app = FastAPI(
    title="Shared Documents API",
    version="0.2.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

# app.include_router(auth_router, prefix="/auth", tags=["auth"])


@app.on_event("startup")
async def on_startup() -> None:
    await mongo_database.init_mongo(app)


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await mongo_database.close_mongo(app)
