from module import local_app_db, local_plate_query
from app_utils import current_milli_time


def add_approved_plate(
        plate: str
):
    if not local_app_db.search(local_plate_query.plate == plate):
        local_app_db.insert(
            {
                'type': 'plate',
                'plate': plate,
                'create_at': current_milli_time()
            }
        )


def get_all_approved_plates():
    return local_app_db.search(local_plate_query.type == 'plate')


def get_approved_plate_by_id(plate):
    return local_app_db.search((local_plate_query.type == 'plate') & (local_plate_query.plate == plate))


def delete_plate(plate):
    local_app_db.remove((local_plate_query.type == 'plate') & (local_plate_query.plate == plate))
