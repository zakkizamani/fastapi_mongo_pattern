from fastapi import FastAPI
# from pymongo import MongoClient
from env.config import Settings
# from app.auth.jwt_handler import signJWT
# from app.auth.jwt_beaerer import jwtBearer
from route.users.user import router_user
from route import login_regiter

# app=FastAPI()
app = FastAPI(
    # openapi_url=Settings().OPENAPI_URL,
    docs_url=Settings().SWAGGER_URL,    
    title=Settings().PROJECT_NAME,
    version=Settings().VERSION,
    description=Settings().DESCRIPTION,
)   


app.include_router(router_user)
app.include_router(
    login_regiter.router,
    prefix="/admin",
    tags=["login&register"],
    responses={404: {"description": "Not found"}},
)




    