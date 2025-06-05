
from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from jose import jwt, JWTError

router = APIRouter()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="auth/token")
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

def get_current_user(token: str = Depends(oauth2_scheme)):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload.get("sub")
    except JWTError:
        return None

@router.get("/")
def get_signals(user: str = Depends(get_current_user)):
    if not user:
        return {"error": "Unauthorized"}
    return [
        {"timestamp": "2025-06-05T12:34:00", "type": "COMPRA", "price": 5412.50},
        {"timestamp": "2025-06-05T12:40:00", "type": "VENDA", "price": 5416.75},
    ]
