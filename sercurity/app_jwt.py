import jwt
from datetime import datetime, timedelta


class Token:
    def __init__(self, access_token: str, refresh_token: str, expire_at, refresh_expire_at):
        self.accessToken = access_token
        self.refreshToken = refresh_token
        self.expireAt = expire_at
        self.refreshExpireAt = refresh_expire_at

    def to_dict(self):
        return {
            "accessToken" : self.accessToken.decode("utf-8"),
            "refreshToken" : self.refreshToken.decode("utf-8"),
            "expireAt" : self.expireAt,
            "refreshExpireAt" : self.refreshExpireAt
        }


class AppJWT:
    @staticmethod
    def __verify(token: str, secret_key: str, algorithms):
        try:
            payload = jwt.decode(token, secret_key, algorithms=algorithms)
            return payload['data']
        except jwt.ExpiredSignatureError:
            return None
        except jwt.InvalidTokenError:
            return None

    @staticmethod
    def __create_key(data, secret_key: str, exp_time_hours: int, algorithm: str):
        expire_at = datetime.utcnow() + timedelta(hours=exp_time_hours)
        token_payload = {
            'data': data,
            'exp': expire_at
        }
        token = jwt.encode(token_payload, secret_key, algorithm=algorithm)
        return token, expire_at

    def __init__(self, secret_key: str, refresh_secret_key: str, algorithm='HS256'):
        self._secret_key = secret_key
        self._refresh_secret_key = refresh_secret_key
        self._algorithm = algorithm

    def create_token(self, data) -> Token:
        access_token = AppJWT.__create_key(data, self._secret_key, 1, 'HS256')
        refresh_token = AppJWT.__create_key(data, self._refresh_secret_key, 24, 'HS256')
        return Token(
            access_token[0],
            refresh_token[0],
            round(access_token[1].timestamp() * 1000),
            round(refresh_token[1].timestamp() * 1000)
        )

    def verify_access_token(self, token: str):
        return AppJWT.__verify(token, self._secret_key, ['HS256'])

    def verify_refresh_token(self, token: str):
        return AppJWT.__verify(token, self._refresh_secret_key, ['HS256'])


