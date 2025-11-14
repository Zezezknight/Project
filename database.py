from typing import Optional

from bson import ObjectId
from dotenv import load_dotenv
import os
from motor.motor_asyncio import AsyncIOMotorClient

load_dotenv()

class Database:
    client: Optional[AsyncIOMotorClient] = None
    db: Optional = None

    MONGO_DSN = os.getenv("MONGO_DSN")
    MONGO_DB = os.getenv("MONGO_DB")
    async def connect_mongo(self):
        """Создаёт Mongo client и индексы (если их ещё нет)."""
        print("MONGO_DSN", self.MONGO_DSN)
        self.client = AsyncIOMotorClient(self.MONGO_DSN)
        self.db = self.client[self.MONGO_DB]


    async def close_mongo(self) -> None:
        if self.client:
            self.client.close()

    async def create_doc(self, collection: str, document: dict):
        created = await self.db[collection].insert_one(document)
        return created

    async def find_doc(self, collection: str, doc_id: str):
        found = await self.db[collection].find_one({"_id": ObjectId(doc_id)})
        return found
mongo_database = Database()
