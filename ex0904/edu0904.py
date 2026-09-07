#0904 교육내용

#format string as f-string
age = 25
name = "Tobi"
txt = f"My name is {name}, i'm {age}"
print(txt)
print("-----")

#
txt1 = 'We are the so-called "Vikings" from the north.'
txt2 = "We are the so-called \"Vikings\" from the north."
print(txt1)
print(txt2)
print("-----")

#
a = "banana"
x = a.center(20)
y = a.center(-10) #음수는 미적용
print(x)
print(y)
print("-----")

#
txt3 = "Hello, welcome to my world."
b = txt3.find("my")
print(b)
print("-----")

#
txt4 = "THIS IS NOW!"
x = txt4.isupper()
y = txt4.islower()
print(x)
print(y)
print("-----")

#
txt5 = "     banana     "
x = txt5
print("of all fruits", x, "is my favorite")

x = txt5.lstrip() #lstrip : left 여백 제거
print("of all fruits", x, "is my favorite")

x = txt5.rstrip() #rstrip : right 여백 제거
print("of all fruits", x, "is my favorite")
print("-----")

#maketrans
#replace와 차이 : 1글자 단위(1:1매핑) 변환, 다수의 특정문자를 치환/제거할때 사용
txt6 = "Hello Eden!"
mytable = str.maketrans("H", "W")
print(txt6.translate(mytable))

mytable1 = str.maketrans("eo", "t1")
print(txt6.translate(mytable1))
print("-----")

#비트 연산자 : (이진)숫자를 비교하는데 사용
# &(AND), |(OR), ^(XOR), ~(NOT), <<(Zero fill left shift), >>(Signed right shift)
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)
print("-----")

#Dictionary : key 와 value 쌍으로 데이터 값을 저장하는데 사용
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.keys()
print(x)
car["color"] = "white" #key 추가
print(x)
y = car.values()
print(y)
z = car.items()
print(z)
print("-----")

#Numpy
import numpy as np

arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))
print(arr[0])
print(arr[2] + arr[3])

#0차원
arr0 = np.array(100)
#1차원
arr1 = np.array([1, 2, 3])
#2차원(행, 열) [1,2,3],[4,5,6]=행 / 1,2,3,4,5,6=열
arr2 = np.array([[1, 2, 3], [4, 5, 6]])
#3차원(면, 행, 열)
arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

#배열의 차원확인
print(arr0.ndim)
print(arr1.ndim)
print(arr2.ndim)
print(arr3.ndim)

#고차원 배열
arr5 = np.array([1, 2, 3, 4], ndmin=5)
print(arr5)
print('number of dimensions :', arr5.ndim)

print('2nd element on 1st row: ', arr2[0, 1])
print(arr3[0, 1, 2])
print(arr3[-1, 0, -2])