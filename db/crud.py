from db.database import base

def get_user_info(id: int):
    return base.get(id)

def get_users():
    return base
