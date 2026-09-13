import streamlit as st
import requests


# FastAPI 서버 주소
API_URL = "http://127.0.0.1:8000"


st.title("🚢 Titanic Passenger Database")


# --------------------
# 전체 승객 조회
# --------------------
st.header("승객 목록")

if st.button("전체 승객 조회"):
    response = requests.get(f"{API_URL}/passengers")

    if response.status_code == 200:
        data = response.json()

        # JSON 데이터를 표 형태로 표시
        st.dataframe(data)
    else:
        st.error("승객 정보를 불러오지 못했습니다.")


# --------------------
# 특정 승객 조회
# --------------------
st.header("승객 조회")

passenger_id = st.number_input(
    "승객 ID",
    min_value=1,
    step=1
)

if st.button("승객 조회"):
    response = requests.get(
        f"{API_URL}/passengers/{passenger_id}"
    )

    if response.status_code == 200:
        st.json(response.json())
    else:
        st.error("해당 승객을 찾을 수 없습니다.")


# --------------------
# 승객 삭제
# --------------------
st.header("승객 삭제")

delete_id = st.number_input(
    "삭제할 승객 ID",
    min_value=1,
    step=1,
    key="delete_id"
)

if st.button("승객 삭제"):
    response = requests.delete(
        f"{API_URL}/passengers/{delete_id}"
    )

    if response.status_code == 200:
        st.success("승객 정보가 삭제되었습니다.")
    else:
        st.error("삭제할 승객을 찾을 수 없습니다.")


# --------------------
# 승객 추가
# --------------------
st.header("승객 추가")

new_id = st.number_input(
    "승객 ID",
    min_value=1,
    step=1,
    key="new_id"
)

name = st.text_input("이름")
sex = st.selectbox("성별", ["male", "female"])
pclass = st.number_input("좌석 등급", min_value=1, max_value=3, step=1)
age = st.number_input("나이", min_value=0.0, step=0.5)
sibsp = st.number_input("형제자매/배우자 수", min_value=0, step=1)
parch = st.number_input("부모/자녀 수", min_value=0, step=1)
ticket = st.text_input("티켓 번호")
fare = st.number_input("운임", min_value=0.0, step=0.1)
cabin = st.text_input("객실 번호")
embarked = st.selectbox("탑승 항구", ["S", "C", "Q"])
survived = st.selectbox("생존 여부", [0, 1])

if st.button("승객 추가"):
    passenger = {
        "pclass": pclass,
        "name": name,
        "sex": sex,
        "age": age,
        "sibsp": sibsp,
        "parch": parch,
        "ticket": ticket,
        "fare": fare,
        "cabin": cabin or None,
        "embarked": embarked,
        "survived": survived
    }

    response = requests.post(
        f"{API_URL}/passengers/{new_id}",
        json=passenger
    )

    if response.status_code == 200:
        st.success("승객이 추가되었습니다.")
    else:
        st.error(response.json()["detail"])


# --------------------
# 승객 수정
# --------------------
st.header("승객 수정")

update_id = st.number_input(
    "수정할 승객 ID",
    min_value=1,
    step=1,
    key="update_id"
)

update_name = st.text_input("이름", key="update_name")
update_age = st.number_input("나이", min_value=0.0, step=0.5, key="update_age")

if st.button("승객 수정"):
    passenger = {
        "pclass": 3,
        "name": update_name,
        "sex": "male",
        "age": update_age,
        "sibsp": 0,
        "parch": 0,
        "ticket": "UNKNOWN",
        "fare": 0,
        "cabin": None,
        "embarked": "S",
        "survived": 0
    }

    response = requests.put(
        f"{API_URL}/passengers/{update_id}",
        json=passenger
    )

    if response.status_code == 200:
        st.success("승객 정보가 수정되었습니다.")
    else:
        st.error("수정할 승객을 찾을 수 없습니다.")