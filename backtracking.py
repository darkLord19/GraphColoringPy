from graph import Graph
color = {}
V = 0
def isSafe(g, v, c):
    for i in range(0, V):
        if i in color:
            if g.vertices[i].has_neighbour(v) and color[i]==c:
                return False
    return True

def setColors(g, v, C):
    for c in range(0, C):
        if isSafe(g, v, c):
            color[v] = c
            if v+1 < V:
                setColors(g, v+1, C)
            else:
                return

def get_chromatic_number_backtracking(g):
    global V
    V = g.V
    global color
    chrom_num = 0
    flag = 1
    for chrom_num in range(1, 6):
        flag = 1
        setColors(g, 0, chrom_num)
        for j in range(0, V):
            if j not in color:
                flag = 0
                break
        if flag == 1:
            break
    print(color)
    return chrom_num, color
