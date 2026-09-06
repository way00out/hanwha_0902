#0903 교육내용
a = " Hello, Wolrd! "
print(len(a)) # len : length 문자열의 길이, list 등 객체의 개수를 셈

print(a[2:5])
print(a[:7])
print(a[2:])
print(a[-5:-2])

print(a.upper()) #대문자 변환
print(a.lower()) #소문자 변환
print(a.strip()) #시작, 끝 공백 제거
print(a.replace("H", "J")) #replace : 문자를 다른 문자로 변환
print(a.replace("o", "t")) #중복되는 문자 모두 변환함
print(a.split(",")) #split : , 기준으로 분리, 기준 문자는 미포함하여 출력, list로 출력
print(a.split("l"))

txt = "THe best things in life are free!"
print("free" in txt)
print("free" not in txt)

#class & object
class Person: #클래스 정의
  def __init__(self, name, age): #클래스 초기화 #__init__ : initialize 객체의 기본값을 설정하거나 속성을 초기화
    self.name = name
    self.age = age

  def greet(self): #매서드
    print("Hello, my name is " + self.name)

  def info(self): #f-string : 문자열 안에 변수나 계산식을 빠르고 직관적으로 넣을 수 있는 문법
    print(f"{self.name}, {self.age}")

  def greet1(self):
    return "Hello, " + self.name

  def welcome(self):
    message = self.greet1()
    print(message + "! Welcome to our website.")

#obj 생성
p1 = Person("Emil", 36)
p2 = Person("Tobi", 24)
p3 = Person("John", 15)

print(p1.name)
print(p1.age)
print(p2.name)
print(p3.age)
print(p1.name, p1.age)
print(p2.age, p3.name)
print(len(p1.name))
p3.greet()
p2.info()
p1.welcome()