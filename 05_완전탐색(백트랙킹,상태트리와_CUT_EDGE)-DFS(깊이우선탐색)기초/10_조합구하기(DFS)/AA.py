import sys

# sys.stdin = open("input.txt", "r")


def DFS(l, s):
    global cnt
    if l == m:
        for j in range(m):
            print(res[j], end=" ")
        print()
        cnt += 1
    else:
        for i in range(s, n + 1):
            res[l] = i
            DFS(l + 1, i + 1)


if __name__ == "__main__":
    n, m = map(int, input().split())
    res = [0] * m
    cnt = 0
    DFS(0, 1)
    print(cnt)