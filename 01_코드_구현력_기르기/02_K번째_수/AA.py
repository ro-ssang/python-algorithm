import sys

# sys.stdin = open("input.txt", "rt")

T = int(input())
for t in range(T):
    n, s, e, k = map(int, input().split())
    arr = list(map(int, input().split()))
    arr = arr[s - 1 : e]
    arr.sort()
    print("#%d %d" % (t + 1, arr[k - 1]))
