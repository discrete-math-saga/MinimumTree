import networkx as nx
from Kruskal import Kruskal
from drawGraph import drawGraph, Point


def defineGraph():
    nodeList = list()
    for i in range(10):
        v = "v" + str(i)
        nodeList.append(v)
    edgeListWithWeight: list[tuple[str, str, float]] = [
        ("v0", "v1", 3),
        ("v0", "v2", 2),
        ("v0", "v3", 3),
        ("v1", "v2", 1),
        ("v1", "v4", 2),
        ("v1", "v5", 1),
        ("v1", "v6", 2),
        ("v2", "v3", 5),
        ("v3", "v6", 1),
        ("v3", "v9", 1),
        ("v4", "v5", 1),
        ("v4", "v7", 3),
        ("v4", "v8", 3),
        ("v5", "v8", 1),
        ("v6", "v8", 2),
        ("v7", "v8", 2),
        ("v8", "v9", 1),
    ]
    edgeLabels = dict()
    positions: dict[str, Point] = {
        "v0": Point(0.2, 0.8),
        "v1": Point(0.2, 0.6),
        "v2": Point(0.4, 0.7),
        "v3": Point(0.6, 0.8),
        "v4": Point(0.2, 0.4),
        "v5": Point(0.4, 0.5),
        "v6": Point(0.6, 0.6),
        "v7": Point(0.4, 0.3),
        "v8": Point(0.6, 0.4),
        "v9": Point(0.8, 0.6),
    }
    G = nx.Graph()
    G.add_nodes_from(nodeList)
    for s, d, w in edgeListWithWeight:
        a = (s, d)
        G.add_edge(s, d, weight=w)
        edgeLabels[a] = str(w)
    return G, positions, edgeLabels


if __name__ == "__main__":
    G, positions, edgeLabels = defineGraph()
    tree:list[tuple[str, str]] = Kruskal(G)
    drawGraph(G, positions, edgeLabels, tree)
    print("end")
