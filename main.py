from __future__ import annotations
from fastapi import FastAPI, Request
from database import fake_documents_db


app = FastAPI(
    title="Shared Documents API",
    version="0.2.0",
    openapi_url="/openapi.json",
    docs_url="/docs",
)

@app.get("/documents")
async def get_user_documents(request: Request):
    user_id = request.headers.get("X-User-ID")
    docs = mongo_database.find_user_docs("docs", user_id)
    return docs
