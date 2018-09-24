from graph import Graph

def get_chromatic_number(g):
    
    chromatic_number = 0
    li = sorted(g.vertices, key=len, reverse=True)
    vertex_color_idx = {0:1}
    available = [True for i in range(0, g.V)]
    for i in range(1, g.V):
        v = li[i]
        for j in v.neighbours:
            if j in vertex_color_idx:
                available[vertex_color_idx[j]] = False
        cr = 0
        for cr in range(0, g.V):
            if available[cr]:
                break
        vertex_color_idx[v.node] = cr
        available = [True for x in range(0, g.V)]

    colored = [-1 for i in range(0,6)]

    for _,value in vertex_color_idx.items():
        colored[value] = 1
    
    for i in colored:
        if i==1:
            chromatic_number += 1
    print(chromatic_number)
    return chromatic_number, vertex_color_idx
