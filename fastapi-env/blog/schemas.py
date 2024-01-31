from pydantic import BaseModel


# création de modéle pour créer une structure de la base de donnée using pydentic modele
class Blog(BaseModel):
    title: str
    body: str


# uses for affichage bien determiner pour seulement title


class User(BaseModel):
    name: str
    email: str
    password: str

class showUser(BaseModel):
    name: str
    email: str
    blogs : list[Blog] = []
    class Config():
        orm_mode = True
class showblog(BaseModel):
    title: str
    body: str
    creator: showUser
    class Config():
        orm_mode = True
class Login(BaseModel):
    username: str
    password: str

class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: str | None = None