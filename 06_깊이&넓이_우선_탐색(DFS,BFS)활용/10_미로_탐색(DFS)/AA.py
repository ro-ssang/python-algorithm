import sys

# sys.stdin = open("input.txt", "r")

"""
미로탐색(DFS)
7*7 격자판 미로를 탈출하는 경로의 가지수를 출력하는 프로그램을 작성하세요. 출발점은 격
자의 (1, 1) 좌표이고, 탈출 도착점은 (7, 7)좌표이다. 격자판의 1은 벽이고, 0은 통로이다. 격
자판의 움직임은 상하좌우로만 움직인다. 미로가 다음과 같다면
출발 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 도착
위의 지도에서 출발점에서 도착점까지 갈 수 있는 방법의 수는 8가지이다.
▣ 입력설명
7*7 격자판의 정보가 주어집니다.
▣ 출력설명
첫 번째 줄에 경로의 가지수를 출력한다.
▣ 입력예제 1 
0 0 0 0 0 0 0
0 1 1 1 1 1 0
0 0 0 1 0 0 0
1 1 0 1 0 1 1
1 1 0 0 0 0 1
1 1 0 1 1 0 0
1 0 0 0 0 0 0
▣ 출력예제 1
8
"""

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def DFS(x, y):
    global cnt
    if x == 6 and y == 6:
        cnt += 1
    else:
        for i in range(4):
            xx = x + dx[i]
            yy = y + dy[i]
            if 0 <= xx < 7 and 0 <= yy < 7 and board[xx][yy] == 0:
                board[xx][yy] = 1
                DFS(xx, yy)
                board[xx][yy] = 0


if __name__ == "__main__":
    board = [list(map(int, input().split())) for _ in range(7)]
    board[0][0] = 1
    cnt = 0
    DFS(0, 0)
    print(cnt)