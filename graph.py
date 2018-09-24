class Vertex:
	node = 0
	neighbours = []

	def __init__(self, n):
		self.node = n
		self.neighbours = []

	def add_neighbour(self, v):
		self.neighbours.append(v)
	
	def __len__(self):
		return len(self.neighbours)

	def has_neighbour(self, n):
		return n in self.neighbours
	

class Graph:
	V = 0
	vertices = []

	def __init__(self, v):
		self.V = v
		for i in range(0,v):
			self.vertices.append(Vertex(i))

	def add_edge(self, u, v):
		self.vertices[u].add_neighbour(v)
		self.vertices[v].add_neighbour(u)