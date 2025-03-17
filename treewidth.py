import networkx as nx
from networkx.algorithms.approximation import treewidth_min_fill_in, treewidth_min_degree
import signal

def signal_handler(signum, frame):
    raise Exception("Timed out!")

def signal_activate(seconds: int):
    signal.signal(signal.SIGALRM, signal_handler)
    signal.alarm(seconds)

def calculate_treewidth_min_fill_in(graph: nx.graph, time_limit: int) -> int:
    """Calculates the treewidth of a graph using the min-fill-in heuristic.
    :param graph: The graph for which you want to calculate the treewidth.
    :param time_limit: The time limit for the treewidth calculation in seconds.
    :return: The estimated treewidth of the graph."""
    signal_activate(time_limit)
    tree_decomp = treewidth_min_fill_in(graph)
    # tree_decomp is a tuple of the form (treewidth, tree decomposition)
    return tree_decomp[0]

def calculate_treewidth_min_degree(graph: nx.graph, time_limit: int) -> int:
    """Calculates the treewidth of a graph using the min-degree heuristic.
    :param graph: The graph for which you want to calculate the treewidth.
    :param time_limit: The time limit for the treewidth calculation in seconds.
    :return: The estimated treewidth of the graph."""
    signal_activate(time_limit)
    tree_decomp = treewidth_min_degree(graph)
    # tree_decomp is a tuple of the form (treewidth, tree decomposition)
    return tree_decomp[0]
