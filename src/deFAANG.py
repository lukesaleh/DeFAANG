import os
import heapq
import pickle
import numpy as np
import pandas as pd
import Knapsack
import GraphClass

class MaxHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = []

    def push(self, stock):
        heapq.heappush(self.heap, (-stock[1], stock[0]))
        if len(self.heap) > self.max_size:
            heapq.heappop(self.heap)

    def pop(self):
        if self.heap:
            return (-heapq.heappop(self.heap)[0], self.heap[0][1])
        else:
            raise IndexError("pop from an empty heap")

    def peek(self):
        if self.heap:
            return (-self.heap[0][0], self.heap[0][1])
        else:
            return None

    def get_heap(self):
        return self.heap

    def print_heap(self):
        print("Values in the max-heap:")
        for value, name in self.heap:
            print(f"Name: {name}, Value: {-value}")


class MinHeap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = []

    def push(self, stock):
        heapq.heappush(self.heap, (stock[1], stock[0]))
        if len(self.heap) > self.max_size:
            heapq.heappop(self.heap)

    def pop(self):
        if self.heap:
            return heapq.heappop(self.heap)
        else:
            raise IndexError("pop from an empty heap")

    def peek(self):
        if self.heap:
            return self.heap[0]
        else:
            return None

    def get_heap(self):
        return self.heap

    def print_heap(self):
        print("Values in the min-heap:")
        for value, name in self.heap:
            print(f"Name: {name}, Value: {value}")


def amount_to_invest(stocks, risk, budget):
    # normalize the value of standard deviations for each of the stocks
    print("Budget allocation: ")
    stock_dict = {}

    if risk:
        # Use items() to iterate over the dictionary
        total_risk = sum(risk_value[1] for name, risk_value in stocks.items())

        for name, risk_value in stocks.items():
            stock_dict[name] = (risk_value[1] / total_risk) * budget
            print(f"{name}: ${stock_dict[name]:.2f}")
    else:
        total_risk = sum(1 / risk_value[1] for name, risk_value in stocks.items())

        for name, risk_value in stocks.items():
            stock_dict[name] = budget * (1 / risk_value[1]) / total_risk
            print(f"{name}: ${stock_dict[name]:.2f}")

def csv_loader(filepath):
    filenames = os.listdir(filepath)
    csv_names = [filename for filename in filenames if filename.endswith('.csv')]
    csv_files = {}
    for name in csv_names:
        df = pd.read_csv(filepath+name)
        csv_files[df.Name.iloc[0]] = df
    return csv_files

def main():
    # pkl_path = os.path.join(os.getcwd(), 'adj_list.pkl')

    # with open(pkl_path, 'rb') as file:
    #     adj_list = pickle.load(file)
    print('Importing csv files into dataframes...')
    project_directory = os.path.dirname(os.path.abspath("main.py"))
    #stocks_directory = os.path.dirname(os.path.abspath(project_directory)) 
    csv_files = csv_loader(project_directory+'\\individual_stocks_5yr\\')
    

    print('Building a graph as adjacency matrix...')
    graph = GraphClass.Graph()
    GraphClass.build_graph(csv_files, graph)

    print('Successfully imported all data and built a graph!')
    clean_stck_data = pd.read_csv(project_directory+'\\clean_data\\stocks_clean.csv')
    budget = float(input("Budget (No spaces or commas): $"))
    stock = input("Pick a stock from which you'd like to draw correlations (Ex: AAPL): ")
    num_stocks = int(input("How many stocks would you like to invest in?: "))
    div = input("What would you like to do? (invest or short): ")
    risk = input("High or low risk investment strategy? (H or L): ")

    stock_dict = {}
    risk_bool = False
    if risk == "H":
        risk_bool = True
    elif risk == "L":
        risk_bool = False
    if div == "short":
        stock_heap = MaxHeap(int(num_stocks))
    elif div == "invest":
        stock_heap = MinHeap(int(num_stocks))

    for stock, correlation in adj_list[stock].items():
        stock_heap.push((stock, correlation))

    for index, row in clean_stck_data.iterrows():
        for stock_tuple in stock_heap.get_heap():
            value, name = stock_tuple
            if row['Name'] == name:
                stock_name = row['Name']
                std_dev = row['StandDev']
                value = row['LastClosingVal']
                stock_dict[stock_name] = (value, std_dev)

    amount_to_invest(stock_dict, risk_bool, budget)
    if risk_bool:
        opt_stocks = Knapsack.knapsack_with_stocks_and_names(stock_dict, int(budget))
        for stock, quantity in opt_stocks.items():
            print(f"{stock} (Quantity: {quantity})")

# Implements the main
if __name__ == "__main__":
    main()
