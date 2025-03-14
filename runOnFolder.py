import os
from treewidth import calculate_treewidth_min_fill_in, calculate_treewidth_min_degree
from incidenceGraphFromFile import read_hypergraph
from typing import Dict

def check_treewidth_of_files_in_folder(folder_path: str) -> Dict[str, Dict[str, int]]:
    treewidths = {}

    for filename in os.listdir(folder_path):
        if filename.endswith(".dat"):
            filepath = os.path.join(folder_path, filename)
            try:
                graph = read_hypergraph(filepath)
                treewidths[filename] = {
                    "min_fill_in": calculate_treewidth_min_fill_in(graph),
                    "min_degree": calculate_treewidth_min_degree(graph)
                }
            except Exception as e:
                print(f"Error processing {filename}: {e}")
                treewidths[filename] = {"error": str(e)}
    return treewidths
