import threading

from app_utils.constants import *
from service import create_user
from service.app import management_server, plates_detect


def init():
    if APP_MODE == 'NEW':
        if os.path.exists(LOCAL_DATABASE_NAME):
            os.remove(LOCAL_DATABASE_NAME)

        create_user(
            APP_DEFAULT_USERNAME,
            APP_DEFAULT_PASSWORD
        )


def run_all_service(services: list):
    for s in services:
        thread = threading.Thread(target=s)
        thread.start()


apps = [
    management_server.run,
    plates_detect.run
]


def main():
    try:
        init()
        # management_server.run()
        run_all_service(apps)
    except Exception as e:
        print(e)
        from service.mqtt import jetson
        jetson.clear()
    



if __name__ == '__main__':
    main()
