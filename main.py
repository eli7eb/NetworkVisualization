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
#video_id = "SMALL_03_10_2024"
video_id = "TEST_2024"
# create a class for the data

class GraphData:
  def __init__(self,author, pred, score, label):
    self.author = author
    self.pred = pred
    self.score = score
    self.label = label

def main_vis():
    # open data file
    cwd = os.path.dirname(__file__)  # get current location of script
    print(f'cwd: {cwd}')
    os.path.join(cwd, 'data')
    # dirname = "/data/"
    filename = dir_name+filename_prefix+video_id+filename_postfix
    # "utf-8"
    #file = open(filename, 'r', encoding="ISO-8859-1")
    #csvreader = csv.reader(file)
    with open(filename, 'r', encoding="ISO-8859-1") as file_obj:

        # Create reader object by passing the file
        # object to DictReader method
        graph_data_list = []
        labeldict = {}
        reader_obj = csv.DictReader(file_obj)
        next(reader_obj)
        # Iterate over each row in the csv file
        # using reader object
        for row in reader_obj:

            # print(row)
            a = row['author']
            labeldict[a] = a
            print ('author: '+a)
            s = row['score']
            print('score: ' + s)
            p = row['pred']
            print('pred: ' + p)
            l = row['label']
            print('label: ' + l)

            dg = GraphData(a, p, s, l)
            graph_data_list.append(dg)

    # create the graph
    print("graph_data_list size " + str(len(graph_data_list)))
    # create empty direction graph
    G2 = nx.star_graph(len(graph_data_list))
    for x in graph_data_list:
        print("AUTHOR " + x.author + " LABEL " + x.label + " SCORE " + x.score)
        G2.add_edge(video_id, str(x.author))
    # populate the graph
    pos = nx.spring_layout(G2, seed=63)  # Seed layout for reproducibility
    colors = range(len(graph_data_list))
    options = {
        "node_color": "#A0CBE2",
        "edge_color": colors,
        "width": 4,
        "edge_cmap": plt.cm.Blues,
        "labels":labeldict,
        "with_labels": True,
    }
    nx.draw(G2, pos, **options)
    plt.show()
    #for x in graph_data_list:
    #    print("AUTHOR " + x.author + " LABEL " + x.label + " SCORE " + x.score)
    #    G2.add_edge(video_id, str(x.author))


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    main_vis()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
