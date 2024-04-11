# This is a sample Python script.

import os
from ast import literal_eval
from datetime import datetime

import matplotlib.pyplot as plt
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import networkx as nx

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
        "surprise": "(151, 0, 0)",
        "joy": "(0, 102, 102)",
        "anger": "(96, 96, 96)",
        "disgust": "(153, 76, 0)",
        "fear": "(153, 0, 76)",
        "sadness": "(153, 153, 0)",
        "neutral": "(0, 102, 0)"
    }
    dict_langfam2color = {k: tuple(map(lambda x: x / 255, literal_eval(v)))
                          for k, v in dict_langfam2color.items()
                          }
    counts = str(len(emotions_list))
    for c in emotions_list:
        graph_colors.append(dict_langfam2color[c.label])
    return graph_colors

# prepare graph data
def prepare_data():
    dict_data = {
        "1":{"author": "A", "score": "1", "pred":"1", "label":"joy", "color": "(151, 0, 0)"},
        "2":{"author": "B", "score": "1", "pred":"1", "label":"anger","color": "(96, 96, 96)"},
        "3":{"author": "C", "score": "1", "pred":"1","label": "disgust", "color": "(153, 76, 0)"},
        "4":{"author": "D", "score": "1", "pred":"1", "label":"fear", "color": "(153, 0, 76)"},
        "5":{"author": "E", "score": "1", "pred":"1", "label":"sadness", "color": "(153, 153, 0)"},
        "6":{"author": "F", "score": "1", "pred":"1", "label": "joy", "color": "(151, 0, 0)"},
        "7":{"author": "G", "score": "1", "pred":"1", "label":"joy", "color": "(151, 0, 0)"},
        "8":{"author": "H", "score": "1", "pred":"1", "label":"fear", "color": "(153, 0, 76)"},
        "9":{"author": "I", "score": "1", "pred":"1", "label": "joy", "color": "(151, 0, 0)"},
        "10":{"author": "J", "score": "1", "pred": "1", "label": "sadness", "color": "(153, 153, 0)"}
    }
    graph_data_list = []
    label_dict = {}

    for x, obj in dict_data.items():
        # print(row)
        print(x)

        a = obj['author']
        label_dict[a] = a
        #print ('author: '+a)
        s = obj['score']
        #print('score: ' + s)
        p = obj['pred']
        #print('pred: ' + p)
        l = obj['label']
        #print('label: ' + l)
        dg = GraphData(a, p, s, l)
        graph_data_list.append(dg)
    return (graph_data_list,label_dict)

def main_vis(show_labels):
    graph_data_list, label_dict = prepare_data()
    print("length "+str(len(graph_data_list)))

    # prepare colors - send dict of labels get dict of colors
    colors = prepare_colors(graph_data_list)
    # construct the data array of tuples
    ego_graph_data = []
    ego_graph_data_index = 1
    first = True
    for x in graph_data_list:
        if bool(first) == False:
            tupple_element = (graph_data_list[0].author, x.author)
            ego_graph_data.append(tupple_element)
        first = False

    # add edges
    # populate the graph
    G2 = nx.Graph()
    G2.add_edges_from(ego_graph_data)
    ego = 'A'
    pos = nx.spring_layout(G2)
    nx.draw(G2, pos, node_color="lavender",
            node_size=800, with_labels=True)

    options = {"node_size": 1200, "node_color": "r"}
    nx.draw_networkx_nodes(G2, pos, nodelist=[ego], **options)
    plt.show()


    # print("graph_data_list size " + str(len(graph_data_list)))
    # options = {
    #     "node_color": "#A0CBE2",
    #     "edge_color": colors,
    #     "width": 4,
    #     "font_size":10,
    #     "node_size": 300, # node size
    #     "edge_cmap": plt.cm.Blues,
    #     "labels":label_dict,
    #     "with_labels": show_labels,
    # }
    # if show_labels:
    #     options["labels"] = label_dict
    # #pos = nx.spring_layout(G2, scale=2, k=1)  # ,k=40,seed=63 Seed layout for reproducibility
    # pos = nx.spring_layout(G2)
    # plt.clf()
    #
    # ego = 'A' # ego_graph_data[0]
    # nx.draw(G2,  pos, **options)
    # nx.draw_networkx_nodes(G2, pos, nodelist=[ego], **options)
    # now = datetime.now()
    # output_graph_file_name = "graph_" + now.strftime("%m_%d_%Y_%H_%M_%S") +".png"
    # cwd = os.path.dirname(__file__)  # get current location of script
    # output_dir_name = "./output/"
    # os.path.join(cwd, 'output')
    #
    # plt.savefig(output_dir_name+output_graph_file_name, dpi=1000)
    # print ('done '+output_graph_file_name)

def start_star_graph():
    print('main_vis')
    main_vis(show_labels=True)


if __name__ == '__main__':
    start_star_graph()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
