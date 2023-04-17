from sys import stdin
from collections import deque

# prob : 14267
# https://www.acmicpc.net/problem/14267


def applause(graph, idx, app_total):
    visited = [False for _ in range(n + 1)]
    queue = deque()
    queue.append(idx)
    while queue:
        current = queue.popleft()
        if not visited[current]:
            visited[current] = True
        for child in graph[current]:
            queue.append(child)
            app_total[child] += app_total[current]


if __name__ == "__main__":
    n, m = map(int, stdin.readline().split())
    workers = list(map(int, stdin.readline().split()))
    graph = [[] for _ in range(n + 1)]
    app_total = [0 for _ in range(n + 1)]
    idx = 1
    for prnt in workers:
        if prnt == -1:
            continue
        graph[prnt].append(idx + 1)
        idx += 1

    for _ in range(m):
        i, w = map(int, stdin.readline().split())
        app_total[i] = w

    applause(graph, 1, app_total)

    for i in range(1, n + 1):
        print(app_total[i], end=" ")
