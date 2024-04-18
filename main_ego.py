# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import csv
import networkx as nx
import matplotlib.pyplot as plt
import os
import re

from ast import literal_eval
from datetime import datetime
from matplotlib.lines import Line2D

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
#video_id = "kEZjV5IwUA0"
# before
# video_id = "BEFORE_04_18_2024"
# after
video_id = "AFTER_04_18_2024"
# tech
# video_id = "TECH_04_18_2024"


#video_id = "TEST_2024"
# create a class for the data

class GraphData:
  def __init__(self,author, pred, score, label):
    self.author = author
    self.pred = pred
    self.score = score
    self.label = label

def get_emotion_for_name(emotions_list,name):
    for e in emotions_list:
        print ("author " + str(e.author) + " name " + name)
        if e.author == name:
            return e.label
    return "neutral"

# pass the label dict - assign color to label
def prepare_colors(g2, emotions_list):
    graph_colors = []

    nodes_colors = []
    dict_langfam2color = {
        "surprise": "(117, 191, 49)",  # green
        "joy": "(218, 253, 186)",  # yellow green
        "anger": "(229, 65, 94)",  # red pink
        "disgust": "(160, 0, 124)",  # purple
        "fear": "(100, 166, 119)",  # green olive
        "sadness": "(105, 147, 214)",  # blue
        "neutral": "(209, 206, 214)"  # light grey
    }
    dict_langfam2color = {k: tuple(map(lambda x: x / 255, literal_eval(v)))
                          for k, v in dict_langfam2color.items()
                          }
    counts = str(len(emotions_list))
    for c in list(g2.edges()):
        edge_emotion = get_emotion_for_name(emotions_list, c[1])
        graph_colors.append(dict_langfam2color[edge_emotion])
    for c in list(g2.nodes()):
        emotion = get_emotion_for_name(emotions_list, c)
        nodes_colors.append(dict_langfam2color[emotion])
        # get the color for the edge
        # get_color_for_emotion(c,emotions_list)
    #graph_colors = [dict_langfam2color[fam] for fam in counts.keys()]
    #for i in range(len(nodes_colors)):
    #    if nodes_colors[i] != graph_colors[i]:
    #        print("Here")
    # nodes_colors = [G2.nodes[node][ATTRIBUTE_NAME] for node in list(G2.nodes())]
    return graph_colors, nodes_colors

# remove author_name @ header and numbers trailers
def prepare_author_name(author_name):
    author_name_stripped = author_name.lstrip('@')
    author_name_no_numbers = re.sub(r'\d+', '', author_name_stripped)
    return author_name_no_numbers

def prepare_data():
    cwd = os.path.dirname(__file__)  # get current location of script
    print(f'cwd: {cwd}')
    os.path.join(cwd, 'data')
    # dirname = "/data/"
    filename = dir_name + filename_prefix + video_id + filename_postfix
    # "utf-8"
    # file = open(filename, 'r', encoding="ISO-8859-1")
    # csvreader = csv.reader(file)
    with open(filename, 'r', encoding="ISO-8859-1") as file_obj:

        # Create reader object by passing the file
        # object to DictReader method
        graph_data_list = []
        label_dict = {}

        reader_obj = csv.DictReader(file_obj)
        # skip the title row
        next(reader_obj)
        # Iterate over each row in the csv file
        # using reader object
        for row in reader_obj:
            if not row:
                continue

            # print(row)
            a = prepare_author_name(row['author'])
            #left_chars_trimmed = text.lstrip('xy')
            label_dict[a] = a
            print('author: ' + a)
            s = row['score']
            print('score: ' + s)
            p = row['pred']
            print('pred: ' + p)
            l = row['label']
            print('label: ' + l)
            dg = GraphData(a, p, s, l)
            graph_data_list.append(dg)
    return (graph_data_list,label_dict)

def save_2_output_file():
    now = datetime.now()
    output_graph_file = "graph_" + now.strftime("%m_%d_%Y_%H_%M_%S") + ".png"
    cwd = os.path.dirname(__file__)  # get current location of script
    print(f'cwd: {cwd}')
    output_dir_name = "./output/"
    os.path.join(cwd, 'output')
    plt.savefig(output_dir_name + output_graph_file, dpi=1000)

def main_vis():

    # prepare data
    graph_data_list, label_dict = prepare_data()
    # create the graph
    print("graph_data_list size " + str(len(graph_data_list)))
    # create empty direction graph
    ego_graph_data = []
    nodes_data_colors = []
    ego_graph_data_index = 1
    first = True
    for x in graph_data_list:
        if bool(first) == False:
            tupple_element = (graph_data_list[0].author, x.author)
            ego_graph_data.append(tupple_element)
        first = False
    G2 = nx.Graph()
    G2.add_edges_from(ego_graph_data)

    ego = graph_data_list[0].author
    pos = nx.spring_layout(G2)

    colors, node_colors = prepare_colors(G2, graph_data_list) #  range(len(graph_data_list))

    center_node_color = (242, 184, 75) # , "node_color": '#F2B84B'
    #options = {"node_size": 1200, "node_color": node_colors}
    options_edges = {"edge_color": colors, "edge_cmap": plt.cm.Blues}
    # fig, axe = plt.subplots(figsize=(12, 7))
    #
    # axe.set_title('Title for NetworkX', loc='center')
    # axe.legend()

    nx.draw(G2, pos, node_color=node_colors,
            node_size=800, font_size=10, with_labels=True)
    nx.draw_networkx_nodes(G2, pos, nodelist=[ego])
    nx.draw_networkx_edges(G2, pos, width=2, **options_edges)

    # "surprise": "(117, 191, 49)",  # green
    # "joy": "(218, 253, 186)",  # yellow green
    # "anger": "(229, 65, 94)",  # red pink
    # "disgust": "(160, 0, 124)",  # purple
    # "fear": "(100, 166, 119)",  # green olive
    # "sadness": "(105, 147, 214)",  # blue
    # "neutral": "(209, 206, 214)"  # light grey
    legend_elements = [Line2D([0], [0], marker='o', color='#75BF31', label='surprise', lw=0,
                              markerfacecolor='#75BF31', markersize=10),
                       Line2D([0], [0], marker='o', color='#DAFDBA', label='joy', lw=0,
                              markerfacecolor='#DAFDBA', markersize=10),
                       Line2D([0], [0], marker='o', color='#E5415E', label='anger', lw=0,
                              markerfacecolor='#E5415E', markersize=10),
                       Line2D([0], [0], marker='o', color='#A0007C', label='disgust', lw=0,
                              markerfacecolor='#A0007C', markersize=10),
                       Line2D([0], [0], marker='o', color='#64A677', label='fear', lw=0,
                              markerfacecolor='#64A677', markersize=10),
                       Line2D([0], [0], marker='o', color='#6993D6', label='sadness', lw=0,
                              markerfacecolor='#6993D6', markersize=10),
                       Line2D([0], [0], marker='o', color='#D1CED6', label='neutral', lw=0,
                              markerfacecolor='#D1CED6', markersize=10)]
    ax = plt.gca()
    ax.legend(handles=legend_elements, loc='upper right')
    plt.show()

    save_2_output_file()

    #prepare colors - send dict of labels get dict of colors
    # colors = prepare_colors(graph_data_list)
    # #colors = range(len(graph_data_list))
    # for x in graph_data_list:
    #     print("AUTHOR " + x.author + " LABEL " + x.label + " SCORE " + x.score)
    #     G2.add_edge(video_id, str(x.author), length=50)
    # # populate the graph
    # pos = nx.spring_layout(G2,k=1)  # ,k=40,seed=63 Seed layout for reproducibility
    #
    # options = {
    #     "node_color": "#A0CBE2",
    #     "edge_color": colors,
    #     "width": 4,
    #     "node_size": 300, # node size
    #     "edge_cmap": plt.cm.Blues,
    #     "labels":label_dict,
    #     "with_labels": True,
    # }
    # nx.draw(G2, pos, **options)
    # now = datetime.now()
    # output_graph_file = "graph_" + now.strftime("%m_%d_%Y_%H_%M_%S") +".png"
    # cwd = os.path.dirname(__file__)  # get current location of script
    # print(f'cwd: {cwd}')
    # output_dir_name = "./output/"
    # os.path.join(cwd, 'output')
    # plt.savefig(output_dir_name+output_graph_file, dpi=1000)
    # print ('done '+output_graph_file)
    # #for x in graph_data_list:
    # #    print("AUTHOR " + x.author + " LABEL " + x.label + " SCORE " + x.score)
    # #    G2.add_edge(video_id, str(x.author))


def start_ego_graph(name):
    # Use a breakpoint in the code line below to debug your script.
    main_vis()

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    start_ego_graph('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
