'''
2차원 리스트 생성과 접근
'''
# 1차원 리스트 생성
#a = [0] * 3
#print(a)

# 2차원 리스트 생성
a = [[0] * 3 for _ in range(3)]
print(a)

# 2차원 리스트 접근
a[0][1] = 1
print(a)
a[1][1] = 2
print(a)

# 2차원 리스트 표처럼 출력하기 1
for x in a:
    print(x)

# 2차원 리스트 표처럼 출력하기 2(대괄호 없애기)
for x in a:
    for y in x:
        print(y, end=" ")
    print()
