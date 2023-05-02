# prob : 1012
# https://www.acmicpc.net/problem/1012

import sys

input = sys.stdin.readline
sys.setrecursionlimit(10000)
t = int(input())


def make_graph(m, n, k):
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1
    return graph


def is_lettuce(h, w, graph, v):
    v[h][w] = True
    for y, x in [[-1, 0], [1, 0], [0, 1], [0, -1]]:
        ny = y + h
        nx = x + w
        if 0 <= ny <= n - 1 and 0 <= nx <= m - 1:
            if graph[ny][nx] and not v[ny][nx]:
                is_lettuce(ny, nx, graph, v)


for _ in range(t):
    lettuce_bug = 0
    m, n, k = map(int, input().split())
    graph = make_graph(m, n, k)
    v = [[False] * m for _ in range(n)]
    for h in range(n):
        for w in range(m):
            if graph[h][w] and not v[h][w]:
                lettuce_bug += 1
                is_lettuce(h, w, graph, v)
    print(lettuce_bug)
