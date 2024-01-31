from fastapi import FastAPI
from typing import Optional
from pydantic import BaseModel

# create instance of fast api
app = FastAPI()
# decorate
@app.get('/')
# function
def index ():
    #return 'comment va tu fast api'
    return  {'data': {'name': 'Sarthak'}}

@app.get('/test')
def test (limit = 10, pub: bool = True, sort: Optional[str] = None):
    if pub == True:
        return {'data': f'{limit} published from the db'}
    else:
        return {'data': f'{limit} not existed from the db'}
    
@app.get('/about')
def about ():
    return {'data': {'about page1'}}

# for blog return string as a default result
@app.get('/blog/{id}')
def about (id): 
    return {'data': id}
# for specification of the entred value in path that should be integer
@app.get('/blog1/{id}')
def about (id : int):
    return {'data': id}


class Item(BaseModel):
    name: str
    description: str | None = None
    price: float
    tax: float | None = None



@app.post("/items/")
async def create_item(item: Item):
    return item
