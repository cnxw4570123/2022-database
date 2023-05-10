# prob : 7576
# https://www.acmicpc.net/problem/7576

import sys
from collections import deque

input = sys.stdin.readline


def BFS(graph, start):  # 탐색이 불가능하면 종료 Queue 생명주기랑 같음
    direction = [[-1, 1, 0, 0], [0, 0, -1, 1]]
    q = deque(start)
    while q:
        current_y, current_x = q.popleft()
        for i in range(4):
            ny = direction[0][i] + current_y
            nx = direction[1][i] + current_x
            if 0 <= ny <= m - 1 and 0 <= nx <= n - 1:
                if not graph[ny][nx]:
                    q.append((ny, nx))
                    graph[ny][nx] = graph[current_y][current_x] + 1


n, m = map(int, input().split())  # 가로, 세로

tomatos = [list(map(int, input().split())) for _ in range(m)]
days = 0
path = []
for h in range(m):
    for w in range(n):
        if tomatos[h][w] == 1:
            path += [(h, w)]  # 출발점,날짜

BFS(tomatos, path)

# BFS 탐색 후 그래프 탐색하면서 0이 있으면 -1
for line in tomatos:
    if 0 in line:
        days = -1
        break
    days = max(days, max(line) - 1)
print(days)
