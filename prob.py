# prob : 1303
# https://www.acmicpc.net/problem/1303

import sys


input = sys.stdin.readline
sys.setrecursionlimit(100000)


def distinguish(h, w, graph, v, color):
    cnt = 0
    for y, x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ny, nx = h + y, w + x
        if 0 <= ny <= m - 1 and 0 <= nx <= n - 1:
            if graph[ny][nx] == color and not v[ny][nx]:
                v[ny][nx] = True
                cnt = cnt + 1 + distinguish(ny, nx, graph, v, color)
    return cnt


w_power, b_power = 0, 0

n, m = map(int, input().split())  # 가로, 세로

war_zone = [input().rstrip() for _ in range(m)]

v = [[False] * n for _ in range(m)]

for h in range(m):
    for w in range(n):
        if war_zone[h][w] == "W":
            if not v[h][w]:
                v[h][w] = True
                w_cnt = 1
                w_cnt += distinguish(h, w, war_zone, v, "W")
                w_power += w_cnt * w_cnt
        else:
            if not v[h][w]:
                v[h][w] = True
                b_cnt = 1
                b_cnt += distinguish(h, w, war_zone, v, "B")
                b_power += b_cnt * b_cnt
print(w_power, b_power)
