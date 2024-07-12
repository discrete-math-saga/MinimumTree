import networkx as nx
from binaryHeap import BinaryHeap
from drawGraph import MyEdge


def JarnikPrim(G: nx.Graph, start: str) -> list[tuple[str, str]]:
    """
    Jarnik-Prim法

    Parameters
    ---
    G : 対象となるネットワーク

    start : 始点
    """
    U: set[str] = {start}  # 始点と接続した頂点の集合
    W: set[str] = set(G.nodes()) - U  # 始点と接続しいていない頂点の集合
    T: list[tuple[str, str]] = list()  # 極大木を構成する弧
    heap = BinaryHeap()  # binary heap
    updateHeap(G, start, U, heap)
    while len(W) > 0:
        anew, w = findArc(U, W, heap)
        U.add(w)
        W.remove(w)
        T.append(anew)
        updateHeap(G, w, U, heap)
    return T


def updateHeap(G: nx.Graph, v: str, V: set[str], heap: BinaryHeap[MyEdge]) -> None:
    """
    binary heapの更新

    Parameters:
    ---
    G : 対象ネットワーク

    v : 注目している頂点

    V : 始点と接続している頂点の集合、vを含む

    heap : ヒープ
    """
    edges = nx.edges(G, v)
    for e in edges:
        (u, v) = e
        if (v not in V) or (u not in V):
            w = G.get_edge_data(u, v, "weight")
            ee = MyEdge(e, w["weight"])
            heap.add(ee)


def findArc(
    U: set[str], W: set[str], heap: BinaryHeap[MyEdge]
) -> tuple[tuple[str, str], str]:
    """
    Uとそれ以外を結ぶ最小の重みの弧を見つける

    Parameters
    ---
    U : 始点と接続している頂点の集合

    W : U以外の頂点の集合

    heap : ヒープ
    """
    anew = None
    w = None
    while anew is None and heap.n > 0:
        candidate = heap.poll()
        if candidate:
            (u, v) = candidate.a
            if (u in U) and (v in W):
                anew = (u, v)
                w = v
            elif (v in U) and (u in W):
                anew = (v, u)
                w = u
    if anew and w:
        return (anew, w)
    else:
        raise Exception("Exception in findArc()")
