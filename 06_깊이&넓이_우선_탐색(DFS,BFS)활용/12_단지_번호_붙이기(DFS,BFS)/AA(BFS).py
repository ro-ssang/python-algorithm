import sys
from collections import deque

# sys.stdin = open("input.txt", "r")


def bfs(x, y):
    board[x][y] = 0
    cnt = 1
    dq = deque()
    dq.append((x, y))
    while dq:
        tmp = dq.popleft()
        for k in range(4):
            xx = tmp[0] + dx[k]
            yy = tmp[1] + dy[k]
            if 0 <= xx < n and 0 <= yy < n and board[xx][yy] == 1:
                cnt += 1
                board[xx][yy] = 0
                dq.append((xx, yy))
    return cnt


dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

n = int(input())
board = [list(map(int, input())) for _ in range(n)]
res = []
for i in range(n):
    for j in range(n):
        if board[i][j] == 1:
            res.append(bfs(i, j))
print(len(res))
res.sort()
for x in res:
    print(x)
