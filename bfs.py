from collections import deque


class Graph:
    def __init__(self, vertex, edges):
        self.vertex = vertex
        self.SIZE = len(vertex)
        self.graph = [[False for _ in range(self.SIZE)] for _ in range(self.SIZE)]
        for edge in edges:
            self.graph[vertex.index(edge[0])][vertex.index(edge[1])] = True
            self.graph[vertex.index(edge[1])][vertex.index(edge[0])] = True


def make_graph():  # directed Graph without weight
    global edges
    # vertex = input("Input vertexs with space: ").split()
    # vertex.sort()
    vertex = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]

    # while True:
    #     edge = input("Input edges with space (vertex vertex weight) (To quit > exit): ")
    #     if edge == "exit" or edge == "EXIT":
    #         break
    #     edges.append(edge.split())

    # edges = []
    edges = [
        ["a", "b"],
        ["a", "c"],
        ["a", "e"],
        ["b", "a"],
        ["b", "c"],
        ["b", "d"],
        ["c", "a"],
        ["c", "b"],
        ["c", "d"],
        ["c", "e"],
        ["d", "b"],
        ["d", "c"],
        ["e", "a"],
        ["e", "c"],
        ["e", "h"],
        ["e", "g"],
        ["f", "c"],
        ["g", "e"],
        ["g", "i"],
        ["h", "e"],
        ["h", "i"],
        ["i", "g"],
        ["i", "h"],
    ]
    g1 = Graph(vertex, edges)
    return g1


def dfs_search(Graph, start, visited):
    """
    _summary_

    Args:
        Graph (Graph): Graph instance
        start (int): certain index of Graph
        visited (list): record visted vertex
    """
    visited = [False for _ in range(Graph.SIZE)]
    stack = [start]
    visited[start] = True  # insert First Vertex

    while stack:  # while  stack is not empty
        v = stack.pop()
        print(Graph.vertex[v], end=" -> ")

        for i in range(Graph.SIZE):
            if Graph.graph[v][i] and not visited[i]:  # if start adjacent
                stack.append(i)
                visited[i] = True
    print("end")


edges = []
g1 = make_graph()
visited = []
dfs_search(g1, 0, visited=visited)
