import jwt
from datetime import datetime, timedelta
from fastapi import status, Depends
from fastapi.exceptions import HTTPException
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30


def create_access_token(data: dict):
    expires_delta = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    expire = datetime.utcnow() + expires_delta
    data.update({"exp": expire})
    encoded_jwt = jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt


def decode_access_token(token: str):
    try:
        decoded_token = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return decoded_token
    except (jwt.exceptions.ExpiredSignatureError, jwt.exceptions.DecodeError):
        raise HTTPException(detail={"Token Expire!"}, status_code=403)


def get_user(
    cred: HTTPAuthorizationCredentials = Depends(HTTPBearer(auto_error=False)),
):
    """It checks the HTTP Bearer token and returns the user if the token is
    valid otherwise raises an authentication exception."""
    if cred is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Bearer authentication required",
            headers={"WWW-Authenticate": 'Bearer realm="auth_required"'},
        )
    try:
        decoded_token = decode_access_token(cred.credentials.split(" ")[-1])
    except Exception as err:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail=f"Invalid authentication credentials. {err}",
            headers={"WWW-Authenticate": 'Bearer error="invalid_token"'},
        ) from err
    return decoded_token
