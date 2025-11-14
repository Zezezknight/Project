from __future__ import annotations

from fastapi import FastAPI

from database import mongo_database
from cache_manager import cache

app = FastAPI(
    title="Shared Documents API",
    version="0.2.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)


@app.on_event("startup")
async def on_startup() -> None:
    await cache.connect()
    await mongo_database.connect_mongo()


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await cache.disconnect()
    await mongo_database.close_mongo()
