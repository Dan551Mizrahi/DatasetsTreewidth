import networkx as nx


def read_hypergraph(path_to_file: str) -> nx.Graph:
    """Reads a hypergraph from a file. Outputs its incidence graph.
    We assume the  file's format is the same as in the Hypergraph Dualization Repository:
    https://research.nii.ac.jp/~uno/dualization.html
    :param path_to_file: str
    :return: nx.Graph"""
    with open(path_to_file, 'r') as f:
        lines = f.readlines()

        hyperedges = []
        vertices = set()
        for line in lines:
            hyperedges.append(tuple([int(x) for x in line.strip().split()]))
            vertices.update(hyperedges[-1])

        max_vertex = max(vertices)

        G = nx.Graph()
        G.add_nodes_from(vertices)

        for i, hyperedge in enumerate(hyperedges):
            hyperedge_id = i + max_vertex + 1
            G.add_node(hyperedge_id)
            for vertex in hyperedge:
                G.add_edge(vertex, hyperedge_id)
    return G