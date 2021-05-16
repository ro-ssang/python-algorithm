'''
문자열과 내장함수
'''
msg = "It is Time"
# 문자열 대문자로 만들기
print(msg.upper())
# 문자열 소문자로 만들기
print(msg.lower())
print(msg)

tmp = msg.upper()
print(tmp)
# 문자열 내장 함수
print(tmp.find("T"))
print(tmp.count("T"))
# slice 하기
print(msg)
print(msg[:2])
print(msg[3:5])

# 문자열의 문자 하나씩 접근하기 1
print(len(msg))
for i in range(len(msg)):
    print(msg[i], end=" ")
print()

# 문자열의 문자 하나씩 접근하기 2
for x in msg:
    print(x, end=" ")
print()


# 대문자만 출력하기
for x in msg:
    if x.isupper():
        print(x, end=" ")
print()

# 소문자만 출력하기
for x in msg:
    if x.islower():
        print(x, end=" ")
print()

# 알파뱃만 출력하기(문자열 공백 제거하기)
for x in msg:
    if x.isalpha():
        print(x, end="")
print()

# 아스키 넘버("A": 65, "Z": 90, "a": 97, "z": 122)
tmp = "AZ"
for x in tmp:
    print(ord(x))

tmp = "az"
for x in tmp:
    print(ord(x))

tmp = 65
print(chr(tmp))
