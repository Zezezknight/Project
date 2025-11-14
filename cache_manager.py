import json
from json import JSONDecodeError
from typing import Optional

import redis.asyncio as aioredis

REDIS_URL = "redis://localhost:6379/0"
class CacheManager:
    """Клиент для работы с Redis."""

    def __init__(self):
        self.client: Optional[aioredis.Redis] = None

    async def connect(self):
        """Подключение к Redis."""
        self.client = aioredis.from_url(REDIS_URL)
    async def disconnect(self):
        """Отключение от Redis."""
        if self.client:
            await self.client.close()

    async def get(self, key: str) -> Optional[dict]:
        """Получает значение из кеша."""
        if self.client:
            try:
                data = await self.client.get(key)
                if data:
                    return json.loads(data)
            except JSONDecodeError:
                return None
        return None


    async def get_user_documents(self, user_id: str) -> Optional[dict]:
        """Получает значение из кеша."""
        if self.client:
            try:
                key = f"user:{user_id}:documents"
                data = await self.client.get(key)
                if data:
                    return json.loads(data)
            except JSONDecodeError:
                return None
        return None

    async def get_shared_documents(self) -> Optional[dict]:
        """Получает значение из кеша."""
        if self.client:
            try:
                key = "shared:documents"
                data = await self.client.get(key)
                if data:
                    return json.loads(data)
            except JSONDecodeError:
                return None
        return None


    async def get_current_document(self, user_id: str, doc_id: str) -> Optional[dict]:
        """Получает значение из кеша."""
        if self.client:
            try:
                key = f"user:{user_id}:document:{doc_id}"
                data = await self.client.get(key)
                if data:
                    return json.loads(data)
            except JSONDecodeError:
                return None
        return None


    async def set_user_documents(self, user_id: str, value: dict):
        """Сохраняет значение в кеш с TTL."""
        if self.client:
            key = f"user:{user_id}:documents"
            await self.client.set(key, json.dumps(value), ex=300)

    async def set_shared_documents(self, value: dict):
        """Сохраняет значение в кеш с TTL."""
        if self.client:
            key = "shared:documents"
            await self.client.set(key, json.dumps(value), ex=120)

    async def set_current_documents(self, value: dict, user_id: str, doc_id: str):
        """Сохраняет значение в кеш с TTL."""
        if self.client:
            key = f"user:{user_id}:document:{doc_id}"
            await self.client.set(key, json.dumps(value), ex=120)


cache = CacheManager()
