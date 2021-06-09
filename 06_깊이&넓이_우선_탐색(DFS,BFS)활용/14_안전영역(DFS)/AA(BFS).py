import sys
from collections import deque

# sys.stdin = open("input.txt", "r")

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def bfs(x, y, h):
    ch[x][y] = 1
    dq = deque()
    dq.append((x, y))
    while dq:
        tmp = dq.popleft()
        for k in range(4):
            xx = tmp[0] + dx[k]
            yy = tmp[1] + dy[k]
            if 0 <= xx < n and 0 <= yy < n and board[xx][yy] > h and ch[xx][yy] == 0:
                ch[xx][yy] = 1
                dq.append((xx, yy))


n = int(input())
board = [list(map(int, input().split())) for _ in range(n)]
res = 0
for h in range(100):
    cnt = 0
    ch = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if board[i][j] > h and ch[i][j] == 0:
                bfs(i, j, h)
                cnt += 1
    res = max(res, cnt)
    if cnt == 0:
        break

print(res)