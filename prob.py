# prob : 1260
# https://www.acmicpc.net/problem/1260

from sys import stdin
from collections import deque

input = stdin.readline


def BFS(graph, idx):
    visited = [False] * (n + 1)
    q = deque()
    q.append(idx)
    while q:
        current = q.popleft()
        if not visited[current]:
            visited[current] = True
            print(current, end=" ")
        for c in range(len(graph[current])):
            if graph[current][c] and not visited[c]:
                q.append(c)


def DFS(graph, idx):
    visited = [False] * (n + 1)
    stack = [idx]
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
            print(current, end=" ")
        for c in range(len(graph[current]) - 1, -1, -1):
            if graph[current][c] and not visited[c]:
                stack.append(c)


n, m, v = map(int, input().split())
graph = [[0] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

DFS(graph, v)
print()
BFS(graph, v)
