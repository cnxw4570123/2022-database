# prob : 13023
# https://www.acmicpc.net/problem/13023

import sys

input = sys.stdin.readline


def DFS(graph, start):
    s = [(start, 0, set())]
    while s:
        current, cnt, v = s.pop()
        if cnt == 4:
            return 1
        if current in v:
            continue
        v.add(current)
        for child in graph[current]:
            if child not in v:
                s.append((child, cnt + 1, set(v)))
    return 0


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
ans = []

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)


for i in range(n):
    if DFS(graph, i) == 1:
        print(1)
        break
else:
    print(0)
