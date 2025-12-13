from collections import defaultdict
import networkx as nx

from networkx import DiGraph

from day11.graph import Graph


def solve2(graph: Graph) -> int:
    G: DiGraph[str] = DiGraph()
    for node in graph.nodes.values():
        for next_node in node.next_nodes:
            G.add_edge(node.name, next_node)

    ordered_nodes: list[str] = list(nx.topological_sort(G))
    
    svr_fft = count_paths(G, ordered_nodes, "svr", "fft")
    fft_dac = count_paths(G, ordered_nodes, "fft", "dac")
    dac_out = count_paths(G, ordered_nodes, "dac", "out")
    
    return svr_fft * fft_dac * dac_out

def count_paths(G: DiGraph[str], ordered_nodes: list[str], from_node: str, to_node: str) -> int:
    count: dict[str, int] = defaultdict(int)
    count[from_node] = 1
    for node in ordered_nodes:
        for next_node in G.successors(node):
            count[next_node] += count[node]
    return count[to_node]
