import sys

# sys.stdin = open("input.txt", "r")

"""
알파코드(DFS)
철수와 영희는 서로의 비밀편지를 암호화해서 서로 주고받기로 했다. 그래서 서로 어떻게 암
호화를 할 것인지 의논을 하고 있다.
영희 : 우리 알파벳 A에는 1로, B에는 2로 이렇게 해서 Z에는 26을 할당하여 번호로 보내기
로 하자.
철수 : 정말 바보같은 생각이군!! 생각해 봐!! 만약 내가 “BEAN"을 너에게 보낸다면 그것을 암
호화하면 25114이잖아!! 그러면 이것을 다시 알파벳으로 복원할 때는 많은 방법이 존재하는 
데 어떻게 할건데... 이것을 알파벳으로 바꾸면 BEAAD, YAAD, YAN, YKD 그리고 BEKD로 
BEAN말고도 5가지나 더 있군.
당신은 위와 같은 영희의 방법으로 암호화된 코드가 주어지면 그것을 알파벳으로 복원하는데 
얼마나 많은 방법인 있는지 구하세요.
▣ 입력설명
첫 번째 줄에 숫자로 암호화된 코드가 입력된다. (코드는 0으로 시작하지는 않는다, 코드의 길
이는 최대 50이다) 0이 입력되면 입력종료를 의미한다.
▣ 출력설명
입력된 코드를 알파벳으로 복원하는데 몇 가지의 방법이 있는지 각 경우를 출력한다. 그 가지
수도 출력한다. 단어의 출력은 사전순으로 출력한다.
▣ 입력예제 1 
25114
▣ 출력예제 1
BEAAD
BEAN
BEKD
YAAD
YAN
YKD
6
"""


def DFS(l, p):
    global cnt
    if l == n:
        cnt += 1
        for j in range(p):
            print(chr(res[j] + 64), end="")
        print()
    else:
        for i in range(1, 27):
            if code[l] == i:
                res[p] = i
                DFS(l + 1, p + 1)
            if i >= 10 and code[l] == i // 10 and code[l + 1] == i % 10:
                res[p] = i
                DFS(l + 2, p + 1)


if __name__ == "__main__":
    code = list(map(int, input()))
    n = len(code)
    res = [0] * n
    code.append(-1)
    cnt = 0
    DFS(0, 0)
    print(cnt)