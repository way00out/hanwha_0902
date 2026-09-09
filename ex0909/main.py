from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

class ItemSchema(BaseModel):
    name: str
    price: float
    desc: str | None = None

item_db: dict[int, dict] = {}
id_counter = 1

#생성
#http://127.0.0.1:8000/items/
@app.post("/items/", status_code=201)
async def create_item(item: ItemSchema):
    global id_counter
    new_item = item.model_dump()
    new_item["id"] = id_counter

    item_db[id_counter] = new_item
    id_counter += 1 #id_counter = id_counter + 1

    return {"message": "생성 완료", "data": new_item}

#전체 조회
#http://127.0.0.1:8000/items/
@app.get("/items/")
async def get_all_items():
    return {"message": "전체 목록 조회 완료", "data": list(item_db.values())}

#단일 조회
#http://127.0.0.1:8000/items/{item_id}
@app.get("/items/{item_id}")
async def get_item(item_id: int):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail= "아이템을 찾을 수 없습니다.")

    return {"messege": "단일 조회 완료", "data": item_db[item_id]}

#수정
#http://127.0.0.1:8000/items/{item_id}
@app.put("/items/{item_id}")
async def update_item(item_id: int, item: ItemSchema):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail= "아이템을 찾을 수 없습니다")

    updated_data = item.model_dump()
    updated_data["id"] = item_id
    item_db[item_id] = updated_data

    return {"messge": "수정 완료", "data": updated_data}

#삭제
@app.delete("/items/{item_id}")
async def delete_item(item_id: int):
    if item_id not in item_db:
        raise HTTPException(status_code=404, detail= "아이템을 찾을 수 없습니다")

    deleted_item = item_db.pop(item_id)
    return {"messege": "삭제 완료", "data": deleted_item}
