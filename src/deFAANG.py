import os
import heapq
import pickle
import numpy as np
import pandas as pd


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
    print("Your optimal portfolio: ")
    total = 0.0
    stock_dict = {}

    # Use items() to iterate over the dictionary
    for name, std_dev in stocks.items():
        total += std_dev

    for name, std_dev in stocks.items():
        stock_dict[name] = (std_dev / total) * budget
        if risk:
            stock_dict[name] = budget - stock_dict[name]
        print(name + ": $" + str(stock_dict[name]))


def main():
    pkl_path = os.path.join(os.getcwd(), 'adj_list.pkl')

    with open(pkl_path, 'rb') as file:
        adj_list = pickle.load(file)

    clean_stck_data = pd.read_csv('../clean_data/stocks_clean.csv')
    budget = float(input("Budget: $"))
    stock = input("Pick a stock for reference: ")
    num_stocks = int(input("How many stocks would you like to invest in?: "))
    div = input("What would you like to do? (invest or short): ")
    risk = input("High or low risk investment strategy? (H or L): ")
    stock_dict = {}
    risk_bool = False
    if risk == "H":
        risk_bool = False
    if risk == "L":
        risk_bool = True
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
                stock_dict[stock_name] = std_dev


 #   stock_heap.print_heap()

    amount_to_invest(stock_dict, risk_bool, budget)




# Implements the main
if __name__ == "__main__":
    main()
