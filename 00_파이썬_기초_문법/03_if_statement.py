'''
조건문 if(분기, 중첩)

x = 5
if x != 7:
    print("Lucky")

# 중첩 if문
x = 9
if x >= 10:
    if x % 2 == 1:
        print("10이상의 홀수")

x = 10
if x > 0:
    if x < 10:
        print("10보다 작은 자연수")

# 10보다 작은 자연수를 구할 때, 중첩 if문 대신 and 연산자를 사용할 수 있다.
x = 7
if x > 0 and x < 10:
    print("10보다 작은 자연수")

# python에서는 0 < x < 10 이 가능하다.
x = 7
if 0 < x < 10:
    print("10보다 작은 자연수")

# 분기문
x = -3
if x > 0:
    print("양수")
else:
    print("음수")
'''
# 다중 if문
x = 50
if x >= 90:
    print('A')
elif x >= 80:
    print('B')
elif x >= 70:
    print("C")
elif x >= 60:
    print("D")
else:
    print("F")
