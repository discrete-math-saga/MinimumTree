import networkx as nx
from binaryHeap import BinaryHeap
from drawGraph import MyEdge


def Kruskal(G: nx.Graph) -> list[tuple[str, str]]:
    """
    Kruskal法

    Parameters
    ---
    G : 対象となるネットワーク
    """

    H = BinaryHeap[MyEdge]()
    for u, v in G.edges:
        a: tuple[str, str] = (u, v)
        w = G.get_edge_data(u, v, "weight")
        e = MyEdge(a, w=w["weight"])
        H.add(e)

    GT = nx.Graph()
    for n in G.nodes():
        GT.add_node(n)

    nodes = G.nodes()
    T: list[tuple[str, str]] = list()
    while len(T) < len(nodes) - 1:
        edge = H.poll()
        if edge:
            (u, v) = edge.a
            anew = None
            while anew is None:
                if isConnected(GT, u, v):
                    edge2 = H.poll()
                    if edge2:
                        (u, v) = edge2.a
                else:
                    anew = edge.a
            print(anew)
            GT.add_edge(u, v)
            T.append(anew)
    return T


def __order(v: str, w: str) -> tuple[str, str]:
    """
    reorder (v,w) in alphabetical
    """
    if w > v:
        return w, v
    return v, w


def isConnected(
    G: nx.Graph, start: str, destination: str
) -> tuple[bool, list[tuple[str, str]]]:
    """
    Return True if the destination node is connected to the start node
    """

    L = list()
    Q: list[tuple[str | None, str]] = [(None, start)]
    A = list()
    while len(Q) > 0:
        s, v = Q.pop(0)
        if v == destination:
            return True, A
        if v not in L:
            if s is not None:
                A.append(__order(s, v))
            for v, w in G.edges(v):
                if __order(v, w) not in Q:
                    Q.append(__order(v, w))
            L.append(v)
    return False, A
