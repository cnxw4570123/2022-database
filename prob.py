# prob : 1018
# https://www.acmicpc.net/problem/1018

import sys

input = sys.stdin.readline
n, m = map(int, input().split())  # 세로, 가로
checker = [input().rstrip() for _ in range(n)]
color = ["W", "B"]
cnt = 0
ans = []
i = j = 0


while i + 7 < n and j + 7 < m:
    left = checker[i][j]
    idx = color.index(left)
    for h in range(i, i + 8):
        for w in range(j, j + 8):  # 가로 한 칸씩 변경
            if color[idx] != checker[h][w]:  # 다시 색칠해야 하면
                cnt += 1
            idx = (idx + 1) % 2  # color안에서 계속 바뀌도록 함
        idx = (idx + 1) % 2  # h 변경, 변을 공유하므로 색 변경

    ans.append(min(cnt, 64 - cnt))
    cnt = 0
    j += 1
    if j + 7 == m:  # 가로의 모든 칸을 탐색하면
        i += 1  # 세로 한 칸 이동
        j = 0  # 가로 초기화

print(min(ans))
