# prob : 3078
# https://www.acmicpc.net/problem/3078

import sys
from collections import deque

input = sys.stdin.readline


n, k = map(int, input().split())
friends = [len(input().rstrip()) for _ in range(n)]
ans = 0

length = [0 for _ in range(21)]

# length와 deque에 k개의 원소 넣어서 준비
q = deque()
for elm in friends[0 : k + 1]:
    length[elm] += 1
    q.append(elm)

idx = k + 1

while q:
    current = q.popleft()
    length[current] -= 1  # 자기 자신 제거
    ans += length[current]
    if idx < n:
        q.append(friends[idx])
        length[friends[idx]] += 1
        idx += 1
print(ans)
