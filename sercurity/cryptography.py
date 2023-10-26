import bcrypt


def encrypt(data: str):
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(data.encode(), salt)
    return hashed_password.decode('utf-8')


def verify(data, encrypted_data):
    return bcrypt.checkpw(data.encode(), encrypted_data.encode())
