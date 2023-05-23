# prob : 14503
# https://www.acmicpc.net/problem/14503
import sys
from collections import deque

input = sys.stdin.readline

direction = ((-1, 0), (0, 1), (1, 0), (0, -1))


def BFS(graph, start, cnt):
    q = deque([start])
    while q:
        y, x, arrow = q.popleft()
        if not graph[y][x]:
            graph[y][x] = 2
            cnt += 1
        for i in range(1, 5):
            nd = (arrow - i + 4) % 4
            dy, dx = direction[nd]
            ny, nx = dy + y, dx + x

            if not graph[ny][nx]:
                q.append((ny, nx, nd))
                break
        else:
            by, bx = direction[arrow]
            ny, nx = y - by, x - bx
            if graph[ny][nx] != 1:
                q.append((ny, nx, arrow))
            else:
                break
    return cnt


n, m = map(int, input().split())  # 세로, 가로
r, c, d = map(int, input().split())  # 세로, 가로, 방향
graph = [list(map(int, input().split())) for _ in range(n)]

cnt = 0
print(BFS(graph, (r, c, d), cnt))
