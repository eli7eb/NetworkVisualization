# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import networkx as nx
import matplotlib.pyplot as plt
import os
from collections import Counter
from ast import literal_eval
from datetime import datetime

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

# pass the label dict - assign color to label
def prepare_colors(emotions_list):
    graph_colors = []
    dict_langfam2color = {
        "surprise": "(151, 0, 0)",  # dark red
        "joy": "(0, 102, 102)",  # dark turquoise
        "anger": "(96, 96, 96)",  # grey
        "disgust": "(153, 76, 0)",  # dark yellow
        "fear": "(153, 0, 76)",  # dark pink
        "sadness": "(153, 153, 0)",  # dark yellow
        "neutral": "(0, 102, 0)"  # dark green
        #"Semetic": "(0, 102, 0)",  # dark green
        #"Slavic": "(0, 153, 153)",  # dark blue/green
        #"SubSaharanAfrica": "(0, 0, 153)",  # dark blue
        #"Turkic": "(76, 0, 153)"  # dark purple
    }
    dict_langfam2color = {k: tuple(map(lambda x: x / 255, literal_eval(v)))
                          for k, v in dict_langfam2color.items()
                          }
    counts = str(len(emotions_list))
    for c in emotions_list:
        graph_colors.append(dict_langfam2color[c.label])
    #graph_colors = [dict_langfam2color[fam] for fam in counts.keys()]

    return graph_colors

def main_vis():
    dict_langfam2color = {
        "surprise": "(151, 0, 0)",  # dark red
        "joy": "(0, 102, 102)",  # dark turquoise
        "anger": "(96, 96, 96)",  # grey
        "disgust": "(153, 76, 0)",  # dark yellow
        "fear": "(153, 0, 76)",  # dark pink
        "sadness": "(153, 153, 0)",  # dark yellow
        "neutral": "(0, 102, 0)"  # dark green
        # "Slavic": "(0, 153, 153)",  # dark blue/green
        # "SubSaharanAfrica": "(0, 0, 153)",  # dark blue
        # "Turkic": "(76, 0, 153)"  # dark purple
    }
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
        label_dict = {}

        reader_obj = csv.DictReader(file_obj)
        next(reader_obj)
        # Iterate over each row in the csv file
        # using reader object
        for row in reader_obj:

            # print(row)
            a = row['author']
            label_dict[a] = a
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
    # prepare colors - send dict of labels get dict of colors
    colors = prepare_colors(graph_data_list)
    #colors = range(len(graph_data_list))
    for x in graph_data_list:
        print("AUTHOR " + x.author + " LABEL " + x.label + " SCORE " + x.score)
        G2.add_edge(video_id, str(x.author))
    # populate the graph
    pos = nx.spring_layout(G2, seed=63)  # Seed layout for reproducibility

    options = {
        "node_color": "#A0CBE2",
        "edge_color": colors,
        "width": 4,
        "node_size": 30,
        "edge_cmap": plt.cm.Blues,
        "labels":label_dict,
        "with_labels": True,
    }
    nx.draw(G2, pos, **options)
    now = datetime.now()
    output_graph_file = "graph_" + now.strftime("%m_%d_%Y_%H_%M_%S") +".png"
    cwd = os.path.dirname(__file__)  # get current location of script
    print(f'cwd: {cwd}')
    output_dir_name = "./output/"
    os.path.join(cwd, 'output')
    plt.savefig(output_dir_name+output_graph_file, dpi=1000)
    #for x in graph_data_list:
    #    print("AUTHOR " + x.author + " LABEL " + x.label + " SCORE " + x.score)
    #    G2.add_edge(video_id, str(x.author))


def start_star_graph(name):
    # Use a breakpoint in the code line below to debug your script.
    main_vis()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_star_graph('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
