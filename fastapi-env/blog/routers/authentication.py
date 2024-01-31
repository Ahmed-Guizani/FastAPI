from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy.orm import Session
from .. import schemas, database, models, Hashing, token

router = APIRouter(
    prefix='/login',
    tags=['Login'])

@router.post('/')
def login(request: OAuth2PasswordRequestForm, db : Session = Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.email == request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'invalid credential')
    # verifying the password
    if not Hashing.Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
                            detail=f'Incorrect password')
    # generate the jwt token and return it
    access_token = token.create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type":"bearer"}
