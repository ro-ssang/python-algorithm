'''
리스트와 내장함수(1)
'''
import random as r

# 리스트 생성하기
a = []
#print(a)
b = list()
#print(b)

# 리스트 초기화하기
a = [1, 2, 3, 4, 5]
#print(a)
#print(a[0])

b = list(range(1, 11))
#print(b)

# 두 개의 리스트 합치기
c = a + b
#print(c)

# 리스트 내장 함수
# 항목 추가하기
print(a)
a.append(6)
print(a)

# 항목 삽입하기
a.insert(3, 7)
print(a)

# 항목 삭제하기(마지막)
a.pop()
print(a)
# 항목 삭제하기(인덱스로)
a.pop(3)
print(a)

# 항목 삭제하기(일치하는)
a.remove(4)
print(a)

# 일치하는 인덱스 출력하기
print(a.index(5))

a = list(range(1, 11))
print(a)
# 합 구하기
print(sum(a))
# 최댓값 최솟값
print(max(a))
print(min(a))
print(min(7, 5))
print(min(7, 3, 5))

# 리스트 랜덤으로 섞기
print(a)
r.shuffle(a)
print(a)

# 리스트 정렬하기(내림차순)
a.sort(reverse=True)
print(a)

# 리스트 정렬하기(오름차순)
a.sort()
print(a)

# 리스트 빈 리스트로 만들기
a.clear()
print(a)
