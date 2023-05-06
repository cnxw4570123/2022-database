# prob : 28015
# https://www.acmicpc.net/problem/28015

import sys

input = sys.stdin.readline


def draw(graph, board, idx, end, color):
    if idx <= end:
        if graph[idx] and graph[idx] != board[idx]:
            board[idx] = color
            draw(graph, board, idx + 1, end, color)


n, m = map(int, input().split())
ans = 0
for _ in range(n):
    line = list(map(int, input().split()))
    board = [0] * m

    while line != board:
        start, end = 0, m - 1
        while start <= end:
            if line[start] != board[start]:
                ans += 1
                draw(line, board, start, end, line[start])
            if line[end] == board[end]:
                end -= 1
            start += 1

print(ans)
