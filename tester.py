from greedy_coloring import *
from backtracking import *
from graph import Graph
import networkx as nx
import matplotlib.pyplot as plt

colors = ['red', 'green', 'blue', 'yellow', 'orange']

in_arr = []
with open('input.txt', 'r') as inp:
    for line in inp:
        in_arr.append(line)

# n = int(input('Enter number of vertex: '))
# e = int(input('Enter number of edges: '))

n = int(in_arr[0].split(' ')[0])
e = int(in_arr[0].split(' ')[1])

g = Graph(n)
G = nx.Graph()
G.add_nodes_from([0, n])

for i in range(1, len(in_arr)):
    # s = input('Enter space seperated vertices representing an edge:\n')
    u = int(in_arr[i].split(' ')[0].strip())
    v = int(in_arr[i].split(' ')[1].strip())
    g.add_edge(u, v)
    G.add_edge(u, v)

chromatic_num_wp, vertex_color_wp = get_chromatic_number(g)
chromatic_num_bt, vertex_color_bt = get_chromatic_number_backtracking(g)

print('Chromatic Number is: ',chromatic_num_wp)
print('Chromatic Number is: ',chromatic_num_bt)

nodelist_wp = []
nodelist_bt = []

for i in range(0,chromatic_num_wp):
   nodelist_wp.append([])

for key, value in vertex_color_wp.items():
   nodelist_wp[value].append(key)

for i in range(0,chromatic_num_bt):
    nodelist_bt.append([])

for key, value in vertex_color_bt.items():
    nodelist_bt[value].append(key)

pos = nx.spring_layout(G)

fig = plt.figure()
st = 'Chromatic Number is: ' + str(chromatic_num_bt)
fig.suptitle(st, fontsize=20, color='r')

plt.subplot(1, 2, 1)
plt.title('Welsh Powell')
for i in range(0, len(nodelist_wp)):
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist_wp[i], node_color=colors[i])

labels = {}
for i in range(0,10):
    labels[i] = i

nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels)

plt.axis('off')

plt.subplot(1, 2, 2)
plt.title('Backtracking')
for i in range(0, len(nodelist_bt)):
    nx.draw_networkx_nodes(G, pos, nodelist=nodelist_bt[i], node_color=colors[i])

labels = {}
for i in range(0,10):
    labels[i] = i

nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos, labels)

plt.axis('off')

plt.show()
