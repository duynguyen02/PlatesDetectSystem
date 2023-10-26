import requests
from app_utils.constants import MQTT_SERVER

CLOSE_THE_DOOR_URL = f"{MQTT_SERVER}/cmnd/HQTRLY3CH/POWER/close3ch?p=iotdhtl"
OPEN_THE_DOOR_URL = f"{MQTT_SERVER}/cmnd/HQTRLY3CH/POWER/open3ch?p=iotdhtl"
STOP_THE_DOOR_URL = f"{MQTT_SERVER}/cmnd/HQTRLY3CH/POWER/stop3ch?p=iotdhtl"


def send_signal(url):
    response = requests.request("GET", url)
    return response.json()['result'] == "OK"


def close_the_door():
    return send_signal(CLOSE_THE_DOOR_URL)


def open_the_door():
    return send_signal(OPEN_THE_DOOR_URL)


def stop_the_door():
    return send_signal(STOP_THE_DOOR_URL)