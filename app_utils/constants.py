from dotenv import load_dotenv
import os
import time

from sercurity import AppJWT

load_dotenv()
ev = dict(os.environ)

HOST_PORT = ev['HOST_PORT']
HOST_NAME = ev['HOST_NAME']

LOCAL_DATABASE_NAME = "DigitalConversionPlates.db"

APP_DEFAULT_USERNAME = ev['APP_DEFAULT_USERNAME']
APP_DEFAULT_PASSWORD = ev['APP_DEFAULT_PASSWORD']
APP_MODE = ev['APP_MODE']

CAMERA_IP = ev['CAMERA_IP']

# MONGO_HOSTNAME = ev['MONGO_HOSTNAME']
# MONGO_USERNAME = ev['MONGO_USERNAME']
# MONGO_PASSWORD = ev['MONGO_PASSWORD']
#
# MONGO_DATABASE_NAME = "DigitalConversionPlates"
# MONGO_USER_COLLECTION = "UserCollection"
# MONGO_PLATES_HISTORY_COLLECTION_NAME = "PlatesHistoryCollection"
# MONGO_APPROVED_PLATES_COLLECTION_NAME = "ApprovedPlatesCollection"
# MONGO_SYSTEM_STATUS_COLLECTION_NAME = "SystemStatusCollection"

JWT_SECRET_KEY = ev['JWT_SECRET_KEY']
JWT_REFRESH_SECRET_KEY = ev['JWT_REFRESH_SECRET_KEY']

MQTT_SERVER = ev['MQTT_SERVER']

OPEN_TIME = ev['OPEN_TIME']


def current_milli_time():
    return round(time.time() * 1000)
