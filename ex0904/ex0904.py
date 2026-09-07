#0904 교육내용

#format string as f-string
age = 25
name = "Tobi"
txt = f"My name is {name}, i'm {age}"
print(txt)

#
txt1 = 'We are the so-called "Vikings" from the north.'
txt2 = "We are the so-called \"Vikings\" from the north."
print(txt1)
print(txt2)

#
a = "banana"
x = a.center(20)
y = a.center(-10) #음수는 미적용
print(x)
print(y)

#
txt3 = "Hello, welcome to my world."
b = txt3.find("my")
print(b)

#
txt4 = "THIS IS NOW!"
x = txt4.isupper()
y = txt4.islower()
print(x)
print(y)

#
txt5 = "     banana     "
x = txt5
print("of all fruits", x, "is my favorite")

x = txt5.lstrip() #lstrip : left 여백 제거
print("of all fruits", x, "is my favorite")

x = txt5.rstrip() #rstrip : right 여백 제거
print("of all fruits", x, "is my favorite")

#maketrans
#replace와 차이 : 1글자 단위(1:1매핑) 변환, 다수의 특정문자를 치환/제거할때 사용
txt6 = "Hello Eden!"
mytable = str.maketrans("H", "W")
print(txt6.translate(mytable))

mytable1 = str.maketrans("eo", "t1")
print(txt6.translate(mytable1))

#비트 연산자 : (이진)숫자를 비교하는데 사용
# &(AND), |(OR), ^(XOR), ~(NOT), <<(Zero fill left shift), >>(Signed right shift)
print(6 & 3)
print(6 | 3)
print(6 ^ 3)
print(~3)
print(3 << 2)
print(8 >> 2)
