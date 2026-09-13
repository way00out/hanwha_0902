#---------타이타닉 승객 정보 조회 프로그램-------------

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pathlib import Path
import json

#FastAPI 서버 생성
app = FastAPI()

#현재 main.py와 같은 폴더에 있는 JSON 파일 경로
DB_FILE = Path(__file__).with_name("titanic_db.json")


#승객 데잍터의 형식을 정의
class Passenger(BaseModel):
    pclass: int
    name: str
    sex: str
    age: float | None = None #나이가 없는 경우 None 허용
    sibsp: int
    parch: int
    ticket: str
    fare: float | None = None #운임이 없는 경우 None 허용
    cabin: str | None = None #객실 번호가 없는 경우 None 허용
    embarked: str
    survived: int | None = None #생존 여부가 없는 경우 None 허용


#JSON 파일에서 데이터를 읽어오는 함수
def load_data():
    with open(DB_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


#데이터를 JSON 파일에 저장하는 함수
def save_data(data):
    with open(DB_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# READ - 전체 승객 조회
@app.get("/passengers")
def get_passengers():
    data = load_data()
    return data["passengers"]


# READ - 특정 승객 조회
@app.get("/passengers/{passenger_id}")
def get_passenger(passenger_id: int):
    data = load_data()
    passenger = data["passengers"].get(str(passenger_id)) #JSON의 ID는 문자열이므로 str()로 변환

    if passenger is None: #해당 ID가 없으면 404 에러
        raise HTTPException(status_code=404, detail="Passenger not found")

    return passenger


# CREATE - 승객 추가
@app.post("/passengers/{passenger_id}")
def create_passenger(passenger_id: int, passenger: Passenger):
    data = load_data()
    passenger_id = str(passenger_id)

    if passenger_id in data["passengers"]: #이미 같은 ID가 존재하면 추가하지 않음
        raise HTTPException(status_code=400, detail="Passenger already exists")

    data["passengers"][passenger_id] = passenger.model_dump() #새로운 승객 추가
    save_data(data) #변경된 데이터를 JSON 파일에 저장

    return {"id": passenger_id, "passenger": passenger}


# UPDATE - 승객 수정
@app.put("/passengers/{passenger_id}")
def update_passenger(passenger_id: int, passenger: Passenger):
    data = load_data()
    passenger_id = str(passenger_id)

    if passenger_id not in data["passengers"]: #해당 ID의 승객이 없으면 404 에러
        raise HTTPException(status_code=404, detail="Passenger not found")

    data["passengers"][passenger_id] = passenger.model_dump() #기존 데이터를 새로운 데이터로 수정
    save_data(data) #수정된 데이터를 JSON 파일에 저장

    return {"id": passenger_id, "passenger": passenger}


# DELETE - 승객 삭제
@app.delete("/passengers/{passenger_id}")
def delete_passenger(passenger_id: int):
    data = load_data()
    passenger_id = str(passenger_id)

    if passenger_id not in data["passengers"]: #해당 ID의 승객이 없으면 404 에러
        raise HTTPException(status_code=404, detail="Passenger not found")

    deleted = data["passengers"].pop(passenger_id) #승객 정보를 삭제하고 삭제된 데이터를 저장
    save_data(data)

    return {"id": passenger_id, "deleted": deleted}
