import pandas as pd
import itertools

import itertools

class AdjacencyMatrixGraph:
    def __init__(self):
        self.adjacency = {}
        self.vertex_count = 0

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}
            for v in self.adjacency:
                if v != vertex:
                    self.adjacency[v][vertex] = 0
                    self.adjacency[vertex][v] = 0
            self.vertex_count += 1
            self.adjacency[vertex] = {v: 0 for v in self.adjacency}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex != to_vertex and self.adjacency[from_vertex][to_vertex] == 0:
            self.adjacency[from_vertex][to_vertex] = weight
            self.adjacency[to_vertex][from_vertex] = weight
        else:
            print("Edge not added.")

    def get_weight(self, from_vertex, to_vertex):
        return self.adjacency[from_vertex][to_vertex]

    def print_matrix(self):
        print("Adjacency Matrix:")
        for vertex, edges in sorted(self.adjacency.items()):
            print(f"{vertex}: {edges}")


class AdjacencyListGraph:
    def __init__(self):
        self.adjacency = {}
        self.vertex_count = 0

    def add_vertex(self, vertex):
        if vertex not in self.adjacency:
            self.adjacency[vertex] = {}

    def add_edge(self, from_vertex, to_vertex, weight):
        if from_vertex != to_vertex and to_vertex not in self.adjacency[from_vertex]:
            self.adjacency[from_vertex][to_vertex] = weight
            self.adjacency[to_vertex][from_vertex] = weight
        else:
            print("Edge not added.")

    def get_weight(self, from_vertex, to_vertex):
        return self.adjacency[from_vertex].get(to_vertex, None)

    def print_list(self):
        print("Adjacency List:")
        for vertex, edges in sorted(self.adjacency.items()):
            print(f"{vertex}: {edges}")


def correlation(stock_a, stock_b):
    corr = stock_a['close'].corr(stock_b['close'])
    return corr


def build_adjacency_matrix(csv_list, graph):
    vertices = csv_list.keys()
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = itertools.combinations(vertices, 2)
    for edge in edges:
        weight = correlation(csv_list[edge[0]], csv_list[edge[1]])
        graph.add_edge(edge[0], edge[1], weight)

    #graph.print_matrix()
    


def build_adjacency_list(csv_list, graph):
    vertices = csv_list.keys()
    for vertex in vertices:
        graph.add_vertex(vertex)
    
    edges = itertools.combinations(vertices, 2)
    for edge in edges:
        weight = correlation(csv_list[edge[0]], csv_list[edge[1]])
        graph.add_edge(edge[0], edge[1], weight)

    #graph.print_list()
    
