import uvicorn
from env.config import Settings

if __name__ == "__main__":
    uvicorn.run("main:app", host=Settings().service_host, port=Settings().service_port, log_level="debug", reload=True)
