import sys

# sys.stdin = open("input.txt", "rt")

n = int(input())
a = list(map(int, input().split()))

ave = int((sum(a) / n) + 0.5)
min = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x - ave)
    if tmp < min:
        min = tmp
        score = x
        res = idx + 1
    elif tmp == min:
        if score < x:
            score = x
            res = idx + 1

print(ave, res)
