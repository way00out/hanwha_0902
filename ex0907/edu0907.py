from datetime import datetime
from pydantic import BaseModel, PositiveInt, ValidationError
from typing import Annotated, Literal
from annotated_types import Gt

#클래스 선언부
class User(BaseModel):
  id : int
  name : str = 'John Doe'
  signup_ts : datetime | None
  tastes : dict[str, PositiveInt]

#데이터
external_data = {
      'id' : 123,
      'signup_ts' : '2019-06-01 12:22',
      'tastes' : {
          'wine' : 9,
          b'cheese' : 7.0,
          'cabbage' : '1',
      },
}

user = User(**external_data) #user 오브젝트 생성

print(user.id)
print(user.model_dump())

external_data2 = {'id': 'not an int', 'tastes': {}}

try:
  User(**external_data2)
except ValidationError as e:
  print(e.errors())

class Fruit(BaseModel):
  name: str
  color: Literal['red', 'green']
  weight: Annotated[float, Gt(0)]
  bazam: dict[str, list[tuple[int, bool, float]]]

print(
    Fruit(
        name= 'Apple',
        color = 'red',
        weight = 4.2,
        bazam= {'foobar': [(1, True, 0.1)]},
    )
)

#직렬화 3가지 방법
class Meeting(BaseModel):
  when: datetime
  where: bytes
  why: str = 'No idea'

m = Meeting(when= '2020-01-01T12:00', where= 'home')
print(m.model_dump(exclude_unset=True)) #사용자가 입력하지 않은 필드 제외 #dict 연관된 파이썬 객체들로 구성된 파이썬으로
print(m.model_dump(exclude={'where'}, mode='json')) #특정 필드 제외 #dict "jsonable"타입으로만 구성된 파이썬으로
print(m.model_dump_json(exclude_defaults=True)) #필드의 현재 값이 기본값과 같으면 제외 #JSON 문자열로 변환