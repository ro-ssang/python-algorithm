'''
함수 만들기

# 함수는 호출전에 선언되어져 있어야 한다.
def add(a, b):
    c = a + b
    print(c)

add(3, 2)
add(5, 7)

# return 하기(return은 값을 반환하고 함수를 종료한다.)
def add(a, b):
    c = a + b
    return c

x = add(3, 2)
print(x)

# python에서는 두 개 이상의 값을 반환할 수 있다.
# 두 개 이상의 값을 반환하면 튜플로 반환된다.
def add(a, b):
    c = a + b
    d = a - b
    return c, d

print(add(3, 2))
'''
# 소수 출력하기
def isPrime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

a = [12, 13, 7, 9, 19]

for y in a:
    if isPrime(y):
        print(y, end=" ")
print()
