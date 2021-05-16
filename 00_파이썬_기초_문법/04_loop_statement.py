'''
반복문(for, while)

# range()는 순차적으로 정수 list를 만든다.
a = range(1, 11)
print(list(a))

# for문
for i in range(1, 11):
    print(i)

# range(start, end, step)
for i in range(10, 0, -1):
    print(i)

# while문
# 1 ~ 10까지 출력
i = 1
while i <= 10:
    print(i)
    i = i + 1

# 10 ~ 1까지 출력
i = 10
while i >= 1:
    print(i)
    i = i - 1

# break
i = 1
while True:
    print(i)
    if i == 5:
        break
    i += 1

# continue
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i)
'''
# for문이 정상적으로 종료되면 else 이후가 실행된다.
# for문에서 break로 비정상적으로 종료하면 else 이후는 실행되지 않는다.
for i in range(1, 11):
    print(i)
    if i > 15:
        break
else:
    print(11)
