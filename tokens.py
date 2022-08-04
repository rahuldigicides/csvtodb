# ! MY simple TOken
import jwt
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer
from datetime import datetime, timedelta
from fastapi import Depends,HTTPException,status, Security
from db import commondbs 

def verify_user(username):
    
    q1='select * from users where email=%s and password=%s'
    q2=(username['usr'], username['paw'])
    result= commondbs(q1, q2)
    if len(result) > 0:
        return username
    else:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,detail="Incorrect username and password",headers={"WWW-Authenticate": "Bearer"},)


# ! Auth Handle File
class AuthHandler():
    security = HTTPBearer()
    secret = 'SECRET'
    
    def encode_token(self, user_id, paw):
        payload = {
            'exp': datetime.utcnow() + timedelta(days=0, minutes=60),
            'iat': datetime.utcnow(),
            'sub': user_id,
            'paw': paw
        }
        return jwt.encode(
            payload,
            self.secret,
            algorithm='HS256'
        )

    def decode_token(self, token):
        try:
            payload = jwt.decode(token, self.secret, algorithms=['HS256'])

            return {"usr": payload['sub'], "paw": payload['paw']}
        except Exception as e:
            raise HTTPException(status_code=401, detail='User is Not Valid')
        except jwt.ExpiredSignatureError:
            raise HTTPException(status_code=401, detail='Signature has expired')
        except jwt.InvalidTokenError as e:
            raise HTTPException(status_code=401, detail='Invalid token')

    def auth_wrapper(self, auth: HTTPAuthorizationCredentials = Security(security)):
       return verify_user(self.decode_token(auth.credentials))



