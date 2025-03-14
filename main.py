import argparse
import os
from runOnFolder import check_treewidth_of_files_in_folder
from tqdm import tqdm

def save_results_csv(results: dict, filepath: str):
    """
    Save the results in a csv file.
    :param results: The estimated treewidths of the hypergraphs.
    :param filepath: A path to save the csv file.
    :return: None
    """
    with open(filepath, "w") as f:
        f.write("hypergraph,min_fill_in,min_degree\n")
        for hypergraph, values in results.items():
            f.write(f"{hypergraph},{values['min_fill_in']},{values['min_degree']}\n")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Calculate treewidth of a hypergraphs dataset in a folder.")
    parser.add_argument("folder_path", type=str, help="Path to the folder containing the hypergraphs.")
    parser.add_argument("-d", "--datasets_folder", action="store_true",
                        help="The path is for a folder that contains multiple datasets folders.")
    parser.add_argument("-p", "--dont_print", action="store_false",
                        help="Don't print the results. Instead save it as a csv file.")
    args = parser.parse_args()

    if args.datasets_folder:
        datasets_dict = dict()
        for folder in tqdm(os.listdir(args.folder_path)):
            folder_path = os.path.join(args.folder_path, folder)
            datasets_dict[folder] = check_treewidth_of_files_in_folder(folder_path)
        if args.dont_print:
            print(datasets_dict)
        else:
            for dataset, results in datasets_dict.items():
                filepath = os.path.join(args.folder_path, f"{dataset}_treewidths.csv")
                save_results_csv(results, filepath)
    else:
        treewidths = check_treewidth_of_files_in_folder(args.folder_path)
        if args.dont_print:
            print(treewidths)
        else:
            save_results_csv(treewidths, os.path.join(args.folder_path, "treewidths.csv"))