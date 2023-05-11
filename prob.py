# prob : 1753
# https://www.acmicpc.net/problem/1753

import sys
import heapq

input = sys.stdin.readline

vertex, edge = map(int, input().split())
graph = [[] for _ in range(vertex + 1)]
k = int(input())
for _ in range(edge):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))  # 거리와 정점


def dijkstra(start):
    costs = [float("INF")] * (vertex + 1)
    costs[start] = 0
    q = []
    heapq.heappush(q, (0, start))  # 간선 가중치와 시작 위치
    while q:
        current_dist, current_pos = heapq.heappop(q)
        for neighbor_dist, neigbor in graph[current_pos]:
            new_dist = neighbor_dist + current_dist
            if new_dist < costs[neigbor]:
                costs[neigbor] = new_dist
                heapq.heappush(q, (new_dist, neigbor))
    return costs


costs = dijkstra(k)  # costs 반환

for i in range(1, vertex + 1):
    if costs[i] == float("inf"):
        print("INF")
    else:
        print(costs[i])
