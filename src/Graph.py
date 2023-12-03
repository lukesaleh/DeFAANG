import pandas as pd
import itertools

class Graph:
    def __init__(self):
        self.adjacency_matrix = {}
        self.vertex_count = 0

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_matrix:
            self.adjacency_matrix[vertex] = {}
            for v in self.adjacency_matrix:
                if v != vertex:
                    self.adjacency_matrix[v][vertex] = 0
                    self.adjacency_matrix[vertex][v] = 0
            self.vertex_count += 1
            self.adjacency_matrix[vertex] = {v: 0 for v in self.adjacency_matrix}

    def add_edge(self, from_vertex, to_vertex, weight):
        # Check for self-loop and parallel edges
        if from_vertex != to_vertex and self.adjacency_matrix[from_vertex][to_vertex] == 0:
            self.adjacency_matrix[from_vertex][to_vertex] = weight
            self.adjacency_matrix[to_vertex][from_vertex] = weight 
        else:
            print("Edge not added.")

    def get_index(self, vertex):
        return self.adjacency_matrix[vertex]

    def print_matrix(self):
        print("Adjacency Matrix:")
        for vertex, edges in sorted(self.adjacency_matrix.items()):
            print(f"{vertex}: {edges}")

    def get_weight(self, from_vertex, to_vertex):
        return self.adjacency_matrix[from_vertex][to_vertex]

def correlation(stock_a, stock_b):
    corr = stock_a['close'].corr(stock_b['close'])
    return corr

def build_graph(csv_list):
    graph = Graph()
    
    vertices = []
    for csv in csv_list:
        vertices.append(csv.Name.iloc[0])
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = itertools.combinations(vertices,2)
    for edge in edges:
        weight = correlation()
        graph.add_edge(edge[0], edge[1])

