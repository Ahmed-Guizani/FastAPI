from fastapi import HTTPException, status
from .. import models, schemas
from sqlalchemy.orm import Session

def all(db: Session):
    blogs = db.query(models.Blog).all()
    return blogs

def create(request: schemas.Blog, db: Session):
    new_blog = models.Blog(title=request.title, body=request.body, user_id=1)
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    return new_blog
# to get specific information from the database
def show(id: int, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).first()
    if not blog:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f'the blog with the id : {id} not existed yet')

    return blog
def destroy(id: int, db: Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id).delete(synchronize_session=False)
    db.commit()

    return 'done'

def updates(id: int, request: schemas.Blog, db : Session):
    blog = db.query(models.Blog).filter(models.Blog.id == id)
    print (models.Blog.id)
    if not blog.first():
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail= f'the id: {id} not found')
    blog.update({models.Blog.title : request.title, models.Blog.body : request.body})
    db.commit()
    return 'updated'