from __future__ import annotations
from fastapi import FastAPI, Request
from database import fake_documents_db
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


@app.on_event("shutdown")
async def on_shutdown() -> None:
    await cache.disconnect()

@app.get("/documents")
async def get_user_documents(request: Request):
    res = []
    user_id = request.headers.get("X-User-ID")
    for doc in fake_documents_db:
        if doc["created_by"] == user_id:
            res.append(doc)
    return res


