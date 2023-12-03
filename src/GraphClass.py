import pandas as pd
import itertools

#Class for adjacency matrix implementation of graph
class AdjacencyMatrixGraph:
    def __init__(self):
        self.adjacency = {}
        self.vertex_count = 0

    def add_vertex(self, vertex):
        #Check if the vertex hasn't already been added
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}
            #Add in a vertex and build out the columns for that row, initialize to 0
            for v in self.adjacency:
                if v != vertex:
                    self.adjacency[v][vertex] = 0
                    self.adjacency[vertex][v] = 0
            self.vertex_count += 1

    def add_edge(self, from_vertex, to_vertex, weight):
        #avoid rewriting lines and causing self loops/parallel edges
        if from_vertex != to_vertex and self.adjacency[from_vertex][to_vertex] == 0:
            self.adjacency[from_vertex][to_vertex] = weight
            self.adjacency[to_vertex][from_vertex] = weight
        else:
            print("Edge not added.")

    #returns correlation of two stocks
    def get_weight(self, from_vertex, to_vertex):
        return self.adjacency[from_vertex][to_vertex]

    #function used mostly for testing
    def print_matrix(self):
        print("Adjacency Matrix:")
        for vertex, edges in sorted(self.adjacency.items()):
            print(f"{vertex}: {edges}")


class AdjacencyListGraph:
    def __init__(self):
        self.adjacency = {}
        self.vertex_count = 0

    def add_vertex(self, vertex):
        #add vertex if it's not already in the graph
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        #avoid rewriting lines and causing self loops/parallel edges
        if from_vertex != to_vertex and to_vertex not in self.adjacency[from_vertex]:
            self.adjacency[from_vertex][to_vertex] = weight
            self.adjacency[to_vertex][from_vertex] = weight
        else:
            print("Edge not added.")

    def get_weight(self, from_vertex, to_vertex):
        #returns correlation of two stocks
        return self.adjacency[from_vertex].get(to_vertex, None)

    #function used mostly for testing
    def print_list(self):
        print("Adjacency List:")
        for vertex, edges in sorted(self.adjacency.items()):
            print(f"{vertex}: {edges}")

#use pandas library to calculate how stocks move with each other
def correlation(stock_a, stock_b):
    corr = stock_a['close'].corr(stock_b['close'])
    return corr

#function to fill adjacency matrix with data from csv files
def build_graph(csv_list, graph):
    vertices = csv_list.keys()
    #first add all vertices, then connect the graphs
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = itertools.combinations(vertices, 2)
    for edge in edges:
        weight = correlation(csv_list[edge[0]], csv_list[edge[1]])
        graph.add_edge(edge[0], edge[1], weight)

    
    
