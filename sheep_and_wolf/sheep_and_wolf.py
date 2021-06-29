import matplotlib.pyplot as plt
import networkx as nx


class Graph:

    def __init__(self, graph):
        self.graph = graph  # residual graph
        self.nodes = len(graph)

    def BFS(self, source, sink, parent):

        visited = [False]*(self.nodes)
        queue = []

        queue.append(source)
        visited[source] = True

        while queue:
            u = queue.pop(0)

            for index, flow in enumerate(self.graph[u]):
                if visited[index] == False and flow > 0:
                    queue.append(index)
                    visited[index] = True
                    parent[index] = u

        return True if visited[sink] else False

    def getDisjointPaths(self, source, sink):
        parent = [-1]*(self.nodes)
        max_flow = 0
        paths = ['#']
        # Augment the flow while there is path from source to sink
        while self.BFS(source, sink, parent):
            path_flow = float("Inf")
            s = sink
            paths.append(s)
            while(s != source):
                path_flow = min(path_flow, self.graph[parent[s]][s])
                s = parent[s]
                paths.append(s)

            paths.append('#')
            max_flow += path_flow

            v = sink
            while(v != source):
                u = parent[v]
                self.graph[u][v] -= path_flow
                self.graph[v][u] += path_flow
                v = parent[v]

        return paths, max_flow


def drawGraph(edges):
    G = nx.DiGraph()
    G.add_edges_from(edges)
    plt.figure(1, figsize=(5, 5))
    nx.draw(G, with_labels=True)
    plt.show()


def showGraphs(paths, edges):
    paths.reverse()

    pathways = []
    for i in paths:
        if i == '#':
            pathways.append([])
        else:
            pathways[-1].append(i)
    print(pathways[:2])

    colors = ['red', 'green']

    G = nx.DiGraph()
    G2 = nx.DiGraph()
    for path, color in zip(pathways[:2], colors):
        for edge in zip(path[:-1], path[1:]):
            G.add_edge(*edge, color=color)

    edge_colors = nx.get_edge_attributes(G, 'color')
    G2.add_edges_from(edges)
    plt.figure(1, figsize=(5, 5))
    nx.draw(G, with_labels=True, edge_color=edge_colors.values())
    plt.figure(2, figsize=(5, 5))
    nx.draw(G2, with_labels=True)
    plt.show()


def main():
    V, E = [int(l) for l in input(
        'Enter the number of vertices and edges: ').split(' ')]
    graph = [[0 for _ in range(V)] for __ in range(V)]
    print("Enter edges: ")
    edges = []
    for _ in range(E):
        x, y = [int(l) for l in input().split(' ')]
        edges.append((x, y))
        graph[x][y] = 1

    graph = Graph(graph)

    source, sink = 0, V-1
    paths, n = graph.getDisjointPaths(source, sink)

    if n > 1:
        print("The sheep is safe!")
        drawGraph(paths, edges)
    else:
        print("Oh no! There are no safe pathways!")
        drawGraph(edges)


if __name__ == "__main__":
    main()
