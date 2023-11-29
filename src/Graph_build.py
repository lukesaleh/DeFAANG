
class CorrelationGraph:
    def __init__(self):
        self.correlation_indices = {}
        self.correlation_matrix = []
        self.stock_names = []

    def add_edge(self, from_vertex, to_vertex, correlation):
        # Add vertices if they don't exist
        if from_vertex not in self.correlation_indices:
            self.correlation_indices[from_vertex] = len(self.stock_names)
            self.stock_names.append(from_vertex)

            # Add a new row and column for the new vertex in the correlation matrix
            for row in self.correlation_matrix:
                row.append(0.0)  # Initialize correlations to 0.0 for the new column
            self.correlation_matrix.append([0.0] * len(self.stock_names))  # Initialize correlations to 0.0 for the new row

        if to_vertex not in self.correlation_indices:
            self.correlation_indices[to_vertex] = len(self.stock_names)
            self.stock_names.append(to_vertex)

            # Add a new row and column for the new vertex in the correlation matrix
            for row in self.correlation_matrix:
                row.append(0.0)  # Initialize correlations to 0.0 for the new column
            self.correlation_matrix.append([0.0] * len(self.stock_names))  # Initialize correlations to 0.0 for the new row

        # Update the correlation in the correlation matrix
        from_index = self.correlation_indices[from_vertex]
        to_index = self.correlation_indices[to_vertex]
        self.correlation_matrix[from_index][to_index] = correlation