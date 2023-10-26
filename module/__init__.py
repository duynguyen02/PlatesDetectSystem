from app_utils import *
from tinydb import TinyDB, Query

# from pymongo import MongoClient

local_app_db = TinyDB(LOCAL_DATABASE_NAME)
local_user_query = Query()
local_plate_query = Query()

jwt_service = AppJWT(
    JWT_SECRET_KEY,
    JWT_REFRESH_SECRET_KEY
)

# mongo_client = MongoClient(f"mongodb://{MONGO_USERNAME}:{MONGO_PASSWORD}@{MONGO_HOSTNAME}")
# mongo_database = mongo_client[MONGO_DATABASE_NAME]
# mongo_approved_plates_collection = mongo_database[MONGO_APPROVED_PLATES_COLLECTION_NAME]
# mongo_user_collection = mongo_database[MONGO_USER_COLLECTION]
