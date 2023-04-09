from sys import stdin
from collections import deque

n = int(stdin.readline().strip())
tree_list = [[] for _ in range(n + 1)]
count = n - 1
while count > 0:
    count -= 1
    node1, node2 = list(map(int, stdin.readline().split()))
    tree_list[node1].append(node2)
    tree_list[node2].append(node1)


visited = [False] * (n + 1)


def BFS(graph, visited, idx):
    prnt_list = [0 for _ in range(n + 1)]
    queue = deque()
    queue.append(idx)
    visited[idx] = True
    while queue:
        current = queue.popleft()
        if not visited[current]:
            visited[current] = True
        for child in graph[current]:
            if not visited[child]:
                prnt_list[child] = current
                queue.append(child)
    return prnt_list


prnt_list = BFS(tree_list, visited, 1)
for val in prnt_list[2:]:
    print(val)
