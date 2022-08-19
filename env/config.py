from pydantic import BaseSettings

from env.setting import load_config

config = load_config()


class Settings(BaseSettings):
    # Project Config
    DEBUG: str = config.get("fastapi", dict())["debug"]
    SECRET_KEY: str = config.get("fastapi", dict())["key"]
    ENVIROMENT: str = config.get("fastapi", dict())["environment"]
    PROJECT_NAME: str = config.get("fastapi", dict())["project-name"]
    VERSION: str = config.get("fastapi", dict())["version"]
    DESCRIPTION: str = config.get("fastapi", dict())["description"]
    OPENAPI_URL: str = config.get("fastapi", dict())["openapi_url"]
    SWAGGER_URL: str = config.get("fastapi", dict())["swagger_url"]
    JWT_SECRET : str = "bb9236d7439b1f0c42c6afb7eb622a31"
    JWT_ALGORITHM : str = "HS256"

    # MongoDb Config
    MGDB_HOST: str = config.get("mongodb", dict())["host"]
    MGDB_PORT: int = config.get("mongodb", dict())["port"]
    MGDB_USERNAME: str = config.get("mongodb", dict())["username"]
    MGDB_PASSWORD: str = config.get("mongodb", dict())["password"]
    MGDB_MAIN: str = config.get("mongodb", dict())["name"]
    
    
    # Service Config
    service_name : str = config.get("service", dict())["name"]
    service_host : str = config.get("service", dict())["host"]
    service_port : int = config.get("service", dict())["port"]

    