#파이썬 다운로드
#파이썬 버전 확인 > cmd : python --version
#파이썬 공간 확인 > cmd : dir

#파이썬 작업환경 가이드
 #가상환경 생성 > cmd : python -m venv <.venv Name>
 #가상환경 활성화 > cmd : <.venv Name>\scripts\activate.bat
    #활성화시 (.venv Name) E:\agent26_DayByDay\day1>
 #개발하기
 #가상환경 비활성화 > .<venv Name>\scripts\deactivate.bat

#파이썬 실행하기(가상환경 활성화 후) > cmd : python test.py

#vscode 가이드
 #파이썬 extionssion 설치
    #vscode 좌측 아이콘 5번째 마켓플레이스 클릭
    #검색창에 python 입력 후 python 설치 > python, python debugger, python environments 설치 완료 확인


#0902 교육내용
print("AI 서비스 백엔드 프로그래밍 실무")
print("-----")
print("파이썬 기본 문법, 시간:8")
print("클래스, 시간:8")
print("데코레이터, 시간:8")
print("예외 처리, 시간:8")
print("로깅, 시간:8")

#변수로 처리
title = "AI 서비스 백엔드 프로그래밍 실무"
a = "파이썬 기본 문법"
b = "클래스"
c = "데코레이터"
d = "예외 처리"
e = "로깅"
time = 8

print(title)
print("-----")
print(a, time, sep=", 시간:") #sep= : separator 값과 값 사이의 들어갈 구분자를 지정
print(b, time, sep=", 시간:")
print(c, time, sep=", 시간:")
print(d, time, sep=", 시간:")
print(e, time, sep=", 시간:")

#list, for 루프
title = "AI 서비스 백엔드 프로그래밍 실무"
list1 = ["파이썬 기본 문법", "클래스", "데코레이터", "예외 처리", "로깅"] #list : 하나의 변수에 여러 항목을 저장
time = 8

print(title)
print("-----")
for x in list1: #for 루프 : list, tuple, dictionary, set, string 같은 시퀀스를 순회
    print(x, time, sep=", 시간:")


#데이터 유형, 형변환
a = 3
x = str(3) #str : string 문자열 변환
y = int(3) #int : integer 정수 변환
z = float(3) # float : floating point number 실수 변환

print(type(a)) #데이터 유형 확인 : type()
print(x)
print(y)
print(z)

#함수 정의
t = "awesome"

def myfunc(): #def : define 새로운 함수 정의
  global t #함수 내부의 변수를 전역 범위에 속하게 함
  t = "fantastic"
  return t + "!!" #return 해당 함수를 호출했을때 최종적으로 불러오는 결과


myfunc() #정의한 함수 호출

print("Python is " + t)
print("Python is " + myfunc())