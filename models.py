from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Literal
from datetime import datetime

PermissionLevel = Literal["read", "write"]
UserRole = Literal["user", "admin"]


class User(BaseModel):
    id: int
    username: str
    role: UserRole
    password: str

# class Document(BaseModel):
#     id: int
#     title: str = Field(..., min_length=1, max_length=200)
#     content: str
#     is_public: bool = False
#     created_by: int
#     category: str = Field(..., min_length=1, max_length=50)

class DocumentCreate(BaseModel):
    title: str = Field(..., min_length=1, max_length=200)
    content: str
    is_public: bool = False
    category: str = Field(..., min_length=1, max_length=50)


class DocumentUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=1, max_length=200)
    content: Optional[str] = None
    is_public: Optional[bool] = None
    category: Optional[str] = Field(None, min_length=1, max_length=50)


class DocumentResponse(BaseModel):
    id: int
    title: str
    content: Optional[str] = None
    category: str
    is_public: bool
    created_by: int
    permission_level: Optional[PermissionLevel] = None
    created_at: datetime
    last_modified: datetime


class DocumentListResponse(BaseModel):
    id: int
    title: str
    category: str
    is_public: bool
    created_by: int
    created_at: datetime
    last_modified: datetime


class SharedDocumentResponse(BaseModel):
    id: int
    title: str
    category: str
    created_by: int
    permission_level: PermissionLevel
    shared_at: datetime


class ShareRequest(BaseModel):
    user_id: int = Field(..., gt=0)
    permission_level: PermissionLevel


class ShareResponse(BaseModel):
    message: str
    cache_invalidated: List[str]


class LoginRequest(BaseModel):
    username: str
    password: str


class LoginResponse(BaseModel):
    access_token: str
    token_type: str
    user_id: int
    username: str
    role: UserRole


class CacheClearResponse(BaseModel):
    message: str
    cleared_keys: List[str]


class Notification(BaseModel):
    type: str
    document_id: int
    document_title: str
    message: str
    timestamp: datetime


class CacheStats(BaseModel):
    total_keys: int
    keys_by_pattern: Dict[str, int]
    memory_usage: Dict[str, Any]