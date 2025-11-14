import hashlib
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

    def _make_key(self, user_id: str, method: str, path: str, query_params: dict) -> str:
        """Формирует ключ кеша."""
        # Сортируем query-параметры для стабильности
        sorted_params = sorted(query_params.items())
        query_str = "&".join(f"{k}={v}" for k, v in sorted_params)
        query_hash = hashlib.sha256(query_str.encode()).hexdigest()[:16]

        return f"cache:{settings.APP_ENV}:{user_id}:{method}:{path}:{query_hash}"

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

    async def get_shared_documents(self,key = "shared:documents") -> Optional[dict]:
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


    async def get_courent_document(self, user_id: str, doc_id: str) -> Optional[dict]:
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

    async def set(self, key: str, value: dict, ttl: int):
        """Сохраняет значение в кеш с TTL."""
        if self.client:
            await self.client.set(key, json.dumps(value), ex=ttl)


cache = CacheManager()