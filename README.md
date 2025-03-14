# DatasetsTreewidth

This repository contains Python code to estimate the treewidth of hypergraphs provided in specific file formats. Treewidth is a graph property that measures how "tree-like" a graph is, and it has significant implications for the complexity of solving certain graph problems.

## Functionality

The code provides the following functionality:

* **Hypergraph Input**: Reads hypergraphs from files. The expected file format is the same as used in the Hypergraph Dualization Repository
    \[[https://research.nii.ac.jp/~uno/dualization.html](https://research.nii.ac.jp/~uno/dualization.html)].  Each line in the file represents a hyperedge, with the vertices in the hyperedge listed as space-separated integers.
* **Incidence Graph Conversion**:  Converts the hypergraph into its incidence graph representation. The incidence graph is a bipartite graph where one set of nodes represents the vertices of the hypergraph, and the other set represents the hyperedges. An edge exists between a vertex and a hyperedge if and only if the vertex is contained in the hyperedge.
* **Treewidth Estimation**:  Estimates the treewidth of the incidence graph using two heuristic algorithms:
    * **Minimum Fill-in**:  A greedy heuristic that iteratively eliminates vertices from the graph, adding edges (filling in) to avoid creating cliques.
    * **Minimum Degree**: Another greedy heuristic that iteratively eliminates vertices with the minimum degree.
* **Batch Processing**: Can process all hypergraph files within a directory, or recursively process hypergraph files within multiple directories.
* **Output**: Results can be printed to the console or saved to a CSV file. The CSV file includes the filename and the treewidths estimated by both heuristics.

## Files

Here's a breakdown of the files in the repository:

* `incidenceGraphFromFile.py`:
    * Reads a hypergraph from a file.
    * Constructs and returns its incidence graph as a `networkx.Graph` object.
* `treewidth.py`:
    * Contains functions to estimate the treewidth of a graph using the minimum fill-in (`calculate_treewidth_min_fill_in`) and minimum degree (`calculate_treewidth_min_degree`) heuristics.
    * Uses the `networkx` library's approximation algorithms for treewidth.
* `runOnFolder.py`:
    * Provides the `check_treewidth_of_files_in_folder` function.
    * This function iterates through all `.dat` files in a specified folder, reads each hypergraph, calculates its treewidth using both heuristics, and stores the results in a dictionary.
* `main.py`:
    * The main script to run the treewidth calculations.
    * Uses `argparse` to handle command-line arguments for specifying the input folder, processing single or multiple datasets folders, and controlling the output method.
    * Uses the `tqdm` library to show a progress bar.
    * Includes the `save_results_csv` function to save the results to a CSV file.
* `README.md`:
    * This file, providing an overview of the repository.

## Usage

### Prerequisites

* Python 3.x
* `networkx`
* `argparse` (standard library)
* `tqdm`

You can install the required packages using pip:

```bash
pip install networkx tqdm
```
### Running the Code

The `main.py` script is the entry point for the program. You can run it from the command line with the following syntax:

```bash
python main.py <folder_path> [-d] [-p]
```
where:
* `<folder_path>`: The path to the folder containing the hypergraph files (.dat files).
* `-d` or `--datasets_folder`: (Optional) If this flag is used, the script expects `<folder_path>` to contain multiple subfolders, each containing hypergraph files dataset. The script will process each subfolder separately.
* `-p` or `--dont_print`: (Optional) By default, results are printed to standard output. If this flag is included, results will be saved to a CSV file instead.

## Examples:

1.  **Process a single folder of hypergraphs and print results to standard output:**

    ```bash
    python main.py path/to/hypergraphs
    ```

2.  **Process multiple datasets (subfolders) and save results to individual CSV files:**

    ```bash
    python main.py path/to/datasets -dp
    ```

    If `path/to/datasets` contains subfolders like `dataset1`, `dataset2`, etc., this will create `dataset1_treewidths.csv`, `dataset2_treewidths.csv`, etc., in the `path/to/datasets` directory.

3.  **Process a single folder and save the results in CSV format:**

    ```bash
    python main.py path/to/hypergraphs -p
    ```
    
    This will create a file named `treewidths.csv` in the `path/to/hypergraphs` directory containing the results.

## Output Format

## Limitations

