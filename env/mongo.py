import asyncio

from loguru import logger
from motor.motor_asyncio import AsyncIOMotorClient

from env.config import Settings


class MongoConnect:
    __instance = None

    def __new__(cls):
        if cls.__instance is None:
            logger.info(f"Initialize mongo instance connection")
            client = AsyncIOMotorClient(
                host=Settings().MGDB_HOST,
                port=Settings().MGDB_PORT,
                username=Settings().MGDB_USERNAME,
                password=Settings().MGDB_PASSWORD,
            )
            client.get_io_loop = asyncio.get_event_loop
            cls.__instance = client
            return client
        else:
            logger.info(f"Use exsisting mongo instance connection: {cls.__instance}")
            return cls.__instance

    def __init__(self):
        self.__instance = None

    def close(self):
        logger.info(f"Close mongo instance connection: {self.__instance}")
        self.__instance.close()


MGDB_CLIENT = MongoConnect()
MGDB_MAIN = MGDB_CLIENT[Settings().MGDB_MAIN]
