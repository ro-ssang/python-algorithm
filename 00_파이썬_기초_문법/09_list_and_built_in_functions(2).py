'''
리스트와 내장함수 (2)
'''
a = [23, 12, 36, 53, 19]
# 리스트 slicing
print(a[:3])
print(a[1:4])

# 리스트 길이
print(len(a))

# 리스트의 값 하나씩 접근하기 1
for i in range(len(a)):
    print(a[i], end=" ")
print()

# 리스트의 값 하나씩 접근하기 2
for x in a:
    print(x, end=" ")
print()

# 홀수 출력하기
for x in a:
    if x % 2 == 1:
        print(x, end=" ")
print()

# 리스트 값을 인덱스와 함께 출력하기(튜플로 출력된다)
for x in enumerate(a):
    print(x)

# 튜플과 리스트의 차이점(튜플은 변경이 불가능하다)
b = (1, 2, 3, 4, 5)
print(b[0])
#b[0] = 7

# enumerate()
for x in enumerate(a):
    print(x[0], x[1])
print()

for index, value in enumerate(a):
    print(index, value)
print()

# all(): 모두를 만족하면 True, 하나라도 만족 못하면 False를 반환한다.
if all(x < 60 for x in a):
    print("YES")
else:
    print("NO")

# any(): 모두를 만족 못하면 False, 하나라도 만족하면 True를 반환한다.
if any(x < 11 for x in a):
    print("YES")
else:
    print("NO")
