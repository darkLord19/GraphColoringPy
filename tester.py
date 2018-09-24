from greedy_coloring import *
from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

colors = ['red', 'green', 'blue', 'yellow', 'orange']

g = Graph(10)

g.add_edge(0, 1)
g.add_edge(1, 2)
g.add_edge(2, 3)
g.add_edge(3, 4)
g.add_edge(4, 5)
g.add_edge(5, 6)
g.add_edge(6, 7)
g.add_edge(7, 8)
g.add_edge(8, 9)
g.add_edge(9, 0)
g.add_edge(0, 7)
g.add_edge(0, 5)
g.add_edge(0, 3)
g.add_edge(2, 8)
g.add_edge(4, 8)

chromatic_num, vertex_color_idx = get_chromatic_number(g)

print('Chromatic Number is: ',chromatic_num)

G = nx.Graph()

G.add_nodes_from([0,10])
G.add_edge(0, 1)
G.add_edge(1, 2)
G.add_edge(2, 3)
G.add_edge(3, 4)
G.add_edge(4, 5)
G.add_edge(5, 6)
G.add_edge(6, 7)
G.add_edge(7, 8)
G.add_edge(8, 9)
G.add_edge(9, 0)
G.add_edge(0, 7)
G.add_edge(0, 5)
G.add_edge(0, 3)
G.add_edge(2, 8)
G.add_edge(4, 8)

nodelist = []
for i in range(0,chromatic_num):
    nodelist.append([])

for key, value in vertex_color_idx.items():
    nodelist[value].append(key)

print(nodelist)

pos = nx.spring_layout(G) 

for i in range(0, len(nodelist)):
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist[i], node_color=colors[i])

labels = {}
for i in range(0,10):
    labels[i] = i

nx.draw_networkx_edges(G, pos, width=2)
nx.draw_networkx_labels(G, pos, labels)

plt.axis('off')
plt.show()