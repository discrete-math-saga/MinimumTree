import matplotlib.pyplot as plt
import networkx as nx
from typing import NamedTuple


class Point(NamedTuple):
    x: float
    y: float


def drawGraph(
    G: nx.Graph,
    position: dict[str, Point],
    edgeLabels: dict[tuple[str, str], str],
    A: list[tuple[str, str]],
) -> None:
    font_size = 24
    node_size = 5000
    edge_width = 5.0
    node_color = "c"
    arrowsize = 50
    plt.figure(figsize=(15, 20), facecolor="white")
    plt.subplot(2, 1, 1)
    nx.draw_networkx_nodes(G, position, node_size=node_size, node_color=node_color)
    nx.draw_networkx_labels(G, position, font_size=font_size)
    nx.draw_networkx_edges(
        G,
        position,
        width=edge_width,
        arrows=True,
        arrowsize=arrowsize,
        node_size=node_size,
    )
    nx.draw_networkx_edge_labels(
        G, position, edge_labels=edgeLabels, font_size=font_size
    )
    plt.axis("off")

    plt.subplot(2, 1, 2)
    nx.draw_networkx_nodes(G, position, node_size=node_size, node_color=node_color)
    nx.draw_networkx_labels(G, position, font_size=font_size)
    nx.draw_networkx_edges(
        G,
        position,
        A,
        width=edge_width,
        edge_color="r",
        arrows=True,
        arrowsize=arrowsize,
        node_size=node_size,
    )

    plt.axis("off")
    plt.show()


def pltInit() -> None:
    """
    Setting fonts
    """
    plt.rcParams["font.family"] = "Times New Roman"
    plt.rcParams["mathtext.fontset"] = "cm"
    plt.rcParams["mathtext.default"] = "it"


class MyEdge:
    """
    Heapに入れるためのクラス、弧aとその重みw
    """

    def __init__(self, a, w):
        self.a = a
        self.w = w

    def __lt__(self, o) -> bool:
        return self.w < o.w

    def __str__(self) -> str:
        return f"{self.a}:{self.w}"
