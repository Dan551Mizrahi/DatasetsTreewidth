import networkx as nx
from networkx.algorithms.approximation import treewidth_min_fill_in, treewidth_min_degree

def calculate_treewidth_min_fill_in(graph: nx.graph) -> int:
    """Calculates the treewidth of a graph using the min-fill-in heuristic."""
    tree_decomp = treewidth_min_fill_in(graph)
    # tree_decomp is a tuple of the form (treewidth, tree decomposition)
    return tree_decomp[0]

def calculate_treewidth_min_degree(graph: nx.graph) -> int:
    """Calculates the treewidth of a graph using the min-degree heuristic."""
    tree_decomp = treewidth_min_degree(graph)
    # tree_decomp is a tuple of the form (treewidth, tree decomposition)
    return tree_decomp[0]
