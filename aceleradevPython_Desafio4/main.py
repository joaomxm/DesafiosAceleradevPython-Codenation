import jwt
from jwt import DecodeError


def create_token(data, secret):
    try:
        jwt_encoded = jwt.encode(data, secret, algorithm="HS256")
        return jwt_encoded

    except Exception as error:
        return error



def verify_signature(token):
    try:
        secret = 'acelera'
        
        jwt_decoded = jwt.decode(
            token,
            key=secret,
            verify=True,
            algorithms='HS256'
            )

        return jwt_decoded

    except DecodeError:
        return {"error": 2}
