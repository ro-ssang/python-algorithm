'''
변수입력과 연산자

# input()을 이용하여 입력을 받을 수 있다.
a = input("숫자를 입력하세요 : ")
print(a)

# split()은 공백을 기준으로 분리시킨다.
a, b = input("숫자를 입력하세요 : ").split()
print(a + b)

# input()을 통해 받은 입력은 문자형이므로 정수형으로 바꾸기 위해 각각 int()를 해준다.
a, b = input("숫자를 입력하세요 : ").split()
a = int(a)
b = int(b)
print(a + b)

# 각각의 변수에 int()를 하지 않고 한번에 int()를 하기 위해 map 함수를 사용한다.
a, b = map(int, input("숫자를 입력하세요 : ").split())
print(a + b)
print(a - b)
print(a * b)
print(a / b)
print(a // b)
print(a % b)
print(a ** b)
'''
# 실수와 정수를 더하면 실수가 출력된다.
a = 4.3
b = 5
c = a + b
print(c)
