import os
from treewidth import calculate_treewidth_min_fill_in, calculate_treewidth_min_degree
from incidenceGraphFromFile import read_hypergraph
from typing import Dict

def check_treewidth_of_files_in_folder(folder_path: str, time_limit: int = 3600) -> Dict[str, Dict[str, int]]:
    """
    Check the treewidth estimations of all hypergraphs in a folder.
    :param folder_path: The path to the folder containing the hypergraphs.
    :param time_limit: The time limit for a single treewidth estimation in .
    """
    treewidths = dict()

    heuristics = {
        "min_fill_in": calculate_treewidth_min_fill_in,
        "min_degree": calculate_treewidth_min_degree,
    }

    for filename in os.listdir(folder_path):
        if filename.endswith(".dat"):
            filepath = os.path.join(folder_path, filename)
            try:
                graph = read_hypergraph(filepath)
            except Exception as e:
                print(f"Error reading {filename}: {e}")
                continue
            treewidths[filename] = dict()
            for heuristic in heuristics:
                try:
                    treewidths[filename][heuristic] = heuristics[heuristic](graph, time_limit)
                except Exception as e:
                    print(f"Error processing {filename} using {heuristic} heuristic: {e}")
                    treewidths[filename][heuristic] = str(e)

    return treewidths
