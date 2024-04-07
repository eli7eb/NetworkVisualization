# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import networkx as nx
import matplotlib.pyplot as plt
import os

# upload the data file
#create the graph data
# call show data as graph
# multiple large
# video_id = "MULTIPLE_03_10_2024"
# multiple test small
dir_name = "./data/"
filename_prefix = "FILENAME_EMOTIONS_"
filename_postfix = "_OUT_ENC.csv"
video_id = "SMALL_03_10_2024"

def main_vis():
    # open data file
    cwd = os.path.dirname(__file__)  # get current location of script
    print(f'cwd: {cwd}')
    os.path.join(cwd, 'data')
    # dirname = "/data/"
    filename = dir_name+filename_prefix+video_id+filename_postfix
    file = open(filename, encoding="utf-8")
    csvreader = csv.reader(file)
    header = []
    header = next(csvreader)
    print(f'cwd: {header}')
    rows = []
    for row in csvreader:
        rows.append(row)
    print("rows")
    print(rows)

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    main_vis()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
