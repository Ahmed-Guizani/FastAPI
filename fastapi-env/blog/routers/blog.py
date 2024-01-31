from fastapi import APIRouter, Depends, status
from .. import schemas, ouath2
from ..database import get_db
from sqlalchemy.orm import Session
from ..repositories import blog


router = APIRouter(
    prefix='/blog',
    tags=['BLogs']
)
@router.get('/')
def all(db: Session=Depends(get_db), get_current_user: schemas.User = Depends(ouath2.get_current_user)):
    return blog.all(db)

@router.post('/', status_code=status.HTTP_201_CREATED)
def create(request: schemas.Blog, db: Session = Depends(get_db)):
    return blog.create(request, db)

@router.get('/{id}', status_code=200, response_model=schemas.showblog)
def show(id: int, db : Session = Depends(get_db)):
    return blog.show(id, db)

@router.delete('/{id}', status_code=status.HTTP_204_NO_CONTENT)
def destroy(id: int, db: Session = Depends(get_db)):
    return blog.destroy(id, db)


@router.put('/{id}', status_code=status.HTTP_202_ACCEPTED)
def updates(id: int, request: schemas.Blog, db : Session = Depends(get_db)):
    return blog.updates(id, db)
