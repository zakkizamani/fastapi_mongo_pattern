from env.mongo import MGDB_MAIN
from pymongo import MongoClient

USER_ADMIN = MGDB_MAIN.user_admin
USER_MEMBER = MGDB_MAIN.user_member
USER_MERCHANT = MGDB_MAIN.user_merchant 

TBL_USER = MGDB_MAIN.users
client = MongoClient('mongodb://localhost:27017')
db = client["manajemen_user"]
users=db.users