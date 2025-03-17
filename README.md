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
    * Because the calculations can be long, we added time limit parameter to the functions.
* `runOnFolder.py`:
    * Provides the `check_treewidth_of_files_in_folder` function.
    * There is a default time limit of 3600 seconds (1 hour) for each hypergraph. You can easily change this parameter in the function call.
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

**Remember** that there is a default time limit of 3600 seconds (1 hour) for each hypergraph. You can easily change this parameter in the function call in `runOnFolder.py`.

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

If the `-p` flag is **not** used, the results are printed to the console as a dictionary. This dictionary is structured as follows:

* **Keys:** The keys of the dictionary are the filenames of the hypergraph files (e.g., `"instance1.dat"`, `"instance2.dat"`).
* **Values:** The values associated with each filename key are themselves dictionaries. These inner dictionaries have two keys:
    * `"min_fill_in"`:  The value associated with this key is the integer treewidth estimate calculated using the minimum fill-in heuristic.
    * `"min_degree"`: The value associated with this key is the integer treewidth estimate calculated using the minimum degree heuristic.

**Example of printed dictionary structure:**

{
"instance1.dat": {
"min_fill_in": 10,
"min_degree": 8
},
"instance2.dat": {
"min_fill_in": 12,
"min_degree": 11
},
"instance3.dat": {
"min_fill_in": 7,
"min_degree": 7
}
}

Otherwise, the results are saved in a CSV file (e.g., `treewidths.csv` or `<dataset_name>_treewidths.csv`). The CSV file has the following header: hypergraph,min_fill_in,min_degree

Each row represents a hypergraph file, and the columns contain:

* `hypergraph`: The name of the hypergraph file.
* `min_fill_in`: The estimated treewidth calculated using the minimum fill-in heuristic.
* `min_degree`: The estimated treewidth calculated using the minimum degree heuristic.



## Limitations

* Heuristics: The treewidth calculations use approximation heuristics. These heuristics do not guarantee to find the exact treewidth, but they provide reasonable estimates.
* File Format: The code is specifically designed to work with hypergraph files formatted as described in the Hypergraph Dualization Repository. It may not work correctly with other hypergraph file formats.
* Computational Cost: Treewidth computation is generally an NP-hard problem. For large hypergraphs, the computation can be time-consuming.