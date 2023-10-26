from module import local_app_db, local_user_query
from app_utils import current_milli_time
from sercurity import encrypt


def create_user(username: str, password: str):
    local_app_db.insert(
        {
            'type': 'user',
            'username': username,
            'password': encrypt(password),
            'create_at': current_milli_time()
        }
    )


def get_user_by_id(username):
    return local_app_db.search((local_user_query.type == 'user') & (local_user_query.username == username))


def get_all_users():
    return local_app_db.search(local_user_query.type == 'user')


def update_user(username, new_password):
    local_app_db.update({'password': new_password}, local_user_query.username == username)


def delete_user(username):
    local_app_db.remove((local_user_query.type == 'user') & (local_user_query.username == username))
