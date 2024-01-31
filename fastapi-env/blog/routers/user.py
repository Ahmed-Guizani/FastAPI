from fastapi import APIRouter, Depends
from .. import schemas
from ..database import get_db
from sqlalchemy.orm import Session
from passlib.context import CryptContext
from ..repositories import user

router = APIRouter(
    prefix='/user',
    tags=['users']
)
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post('/')
def create_user(request: schemas.User, db : Session = Depends(get_db)):
    return user.create_user(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.showUser)
def show(id: int, db : Session = Depends(get_db)):
    return user.show(id, db)