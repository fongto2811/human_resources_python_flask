import jwt
import datetime


def encode_auth_token(app, user_id):
    current_time = datetime.datetime.utcnow()
    try:
        payload = {
            'exp': current_time +
            datetime.timedelta(hours=23-current_time.hour, minutes=59 -
                               current_time.minute, seconds=60-current_time.second),
            'iat': current_time,
            'sub': user_id
        }
        return jwt.encode(
            payload,
            app.config.get('SECRET_KEY'),
            algorithm='HS256'
        )
    except Exception as e:
        return e


@staticmethod
def decode_auth_token(app, auth_token):
    try:
        payload = jwt.decode(auth_token, app.config.get(
            'SECRET_KEY'), algorithms=['HS256'])
        return payload['sub']
    except jwt.ExpiredSignatureError:
        return 'Signature expired. Please log in again.'
    except jwt.InvalidTokenError:
        return 'Invalid token. Please log in again.'
