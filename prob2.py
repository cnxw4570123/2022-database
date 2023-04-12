from sys import stdin


def DFS(graph, idx):
    visited = [False for _ in range(n + 1)]
    cost = [0 for _ in range(n + 1)]
    stack = [idx]
    visited[idx] = True
    while stack:
        current = stack.pop()
        if not visited[current]:
            visited[current] = True
        for child, len in graph[current]:
            if not visited[child]:
                stack.append(child)
                cost[child] += cost[current] + len
    max_val = max(cost)
    index = cost.index(max_val)
    return (index, max_val)


n = int(stdin.readline().strip())
graph = [[] for _ in range(n + 1)]
count = n
while count > 0:
    count -= 1
    v_list = list(map(int, stdin.readline().split()))
    for idx in range(len(v_list) // 2 - 1):
        v = (idx * 2) + 1
        v_len = (idx + 1) * 2
        graph[v_list[0]].append([v_list[v], v_list[v_len]])

node, cost = DFS(graph, 1)
node2, cost2 = DFS(graph, node)

print(max(cost, cost2))
