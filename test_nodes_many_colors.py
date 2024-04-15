import matplotlib.pyplot as plt
import networkx as nx

G = nx.cubical_graph()
pos = nx.spring_layout(G)

nodes = {
    'r': [1, 3, 5],
    'b': [0, 2],
    'g': [4]
}
for node_color, nodelist in nodes.items():
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist, node_color=node_color)

labels = {x: x for x in G.nodes}
nx.draw_networkx_labels(G, pos, labels, font_size=16, font_color='w')
plt.show()
