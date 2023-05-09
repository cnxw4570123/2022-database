import sys
from collections import deque

input = sys.stdin.readline


def bfs(graph, start, end):  # 시작 위치부터 도착까지 필요한 체력을 v에 삽입
    q = deque([[start, graph[0][0], [start]]])  # 시작 위치와 체력 그리고 길
    v = []
    while q:
        current, hp, path = q.popleft()
        if current == end:
            v.append(hp)
        for dy, dx in [[-1, 0], [1, 0], [0, -1], [0, 1]]:  # 인접 노드로 이동
            ny = dy + current[0]
            nx = dx + current[1]
            if 0 <= ny <= n - 1 and 0 <= nx <= n - 1:  # 탐색 가능한 노드면
                if [ny, nx] not in path:
                    q.append([[ny, nx], hp + graph[ny][nx], path + [[ny, nx]]])

    return v


n = int(input())  # n * n 던전크기

dungeon = [list(map(int, input().split())) for _ in range(n)]

route = bfs(dungeon, [0, 0], [n - 1, n - 1])


print(min(route))
