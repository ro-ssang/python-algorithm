import sys

# sys.stdin = open("input.txt", "r")

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0, 0)
dy = [0] * (n + 1)
dy[1] = 1
res = 0
for i in range(2, n + 1):
    for j in range(1, n + 1):
        if arr[j] == i:
            max = 0
            for k in range(j - 1, 0, -1):
                if arr[k] < i and dy[arr[k]] > max:
                    max = dy[arr[k]]
            dy[i] = max + 1
            if dy[i] > res:
                res = dy[i]
            break
print(res)