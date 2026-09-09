from fastapi import FastAPI
from pydantic import BaseModel
from enum import Enum

app = FastAPI()

class Item(BaseModel):
    name: str
    price: float
    is_offer: bool | None = None

#Request URL : http://127.0.0.1:8000/
@app.get("/")
def read_root():
    return {"Hello": "World"}

#http://127.0.0.1:8000/items/123?q=xyz
@app.get("/items/{item_id}")
def read_item(item_id: int, q: str | None = None):
    return {"item_id": item_id, "q": q}

#http://127.0.0.1:8000/items/123
@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}


#http://127.0.0.1:8000/users/me
@app.get("/users/me")
async def ream_user_me():
    return {"user_id": "the current user"}

#http://127.0.0.1:8000/users/abc
@app.get("/users/{user_id}")
async def read_user(user_id: str):
    return {"user_id": user_id}

@app.get("/users") #경로가 먼저 매칭되기 때문에 첫번째 것이 항상 사용됨
async def read_users():
    return ["Rick", "Morty"]

@app.get("/users") #고로, return값 미표시
async def read_users2():
    return ["Bean", "Elfo"]



class ModelName(str, Enum):
    an = "alexnet"
    rn = "resnet"
    ln = "lenet"
    기타 = "기타"

#http://127.0.0.1:8000/models/alexnet
@app.get("/models/{model_name}")
async def get_model(model_name: ModelName):

    #key 요청 시, 값을 리턴
    if model_name is ModelName.an:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}

    #값 요청 시, key를 리턴
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}

    #그 외
    return {"model_name": model_name, "message": "Have some residuals"}



fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]

#http://127.0.0.1:8000/items/?skip=0&limit=10
@app.get("/items/")
async def read_item(skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit] #=[0 : 10] 범위연산자

#http://127.0.0.1:8000/items2/test?q=TEST
@app.get("/items2/{item_id}")
async def read_item(item_id: str, q: str | None = None):
    if q:
        return {"ritem_id": item_id, "q": q}
    return {"item_id": item_id}
