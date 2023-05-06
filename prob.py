# prob : 14502
# https://www.acmicpc.net/problem/14502

import sys
import copy

input = sys.stdin.readline
sys.setrecursionlimit(10000)


def infected_route(h, w, graph, v):
    for y, x in [[-1, 0], [1, 0], [0, -1], [0, 1]]:
        ny = h + y
        nx = w + x
        if 0 <= ny <= n - 1 and 0 <= nx <= m - 1:
            if not v[ny][nx] and not graph[ny][nx]:
                v[ny][nx] = True
                graph[ny][nx] = 2
                infected_route(ny, nx, graph, v)


n, m = map(int, input().split())  # 세로, 가로
ans = 0
graph = [list(map(int, input().split())) for _ in range(n)]

for i in range(n * m - 2):
    if graph[i // m][i % m]:
        continue
    for j in range(i + 1, n * m - 1):
        if graph[j // m][j % m]:
            continue
        for k in range(j + 1, n * m):
            if graph[k // m][k % m]:
                continue
            graph_copy = copy.deepcopy(graph)
            (
                graph_copy[i // m][i % m],
                graph_copy[j // m][j % m],
                graph_copy[k // m][k % m],
            ) = (1, 1, 1)
            v = [[False] * m for _ in range(n)]
            for h in range(n):
                for w in range(m):
                    if graph_copy[h][w] == 2 and not v[h][w]:
                        infected_route(h, w, graph_copy, v)
            safe_zone = 0
            for line in graph_copy:
                safe_zone += line.count(0)
            ans = max(ans, safe_zone)
            # print(f"i, j, k = {i, j, k}safe_zone = {safe_zone}")
print(ans)
