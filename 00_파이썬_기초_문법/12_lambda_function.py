'''
람다 함수

# 일반 함수
def plus_one(x):
    return x + 1

print(plus_one(1))

# 람다
plus_two = lambda x: x + 2
print(plus_two(1))
'''
# 람다 활용법
def plus_one(x):
    return x + 1

a = [1, 2, 3]
print(list(map(plus_one, a)))
print(list(map(lambda x: x + 1, a)))
