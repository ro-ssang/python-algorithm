import sys

# sys.stdin = open("input.txt", "rt")

n, k = map(int, input().split())
arr = list(map(int, input().split()))
result = set()

for x in range(n - 2):
    for y in range(x + 1, n - 1):
        for z in range(y + 1, n):
            result.add(arr[x] + arr[y] + arr[z])

result = list(result)
result.sort(reverse=True)
print(result[k - 1])