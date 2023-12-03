import os
import pandas as pd
import time
import Knapsack
import GraphClass
import Heaps

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
    #store all data frames in a dictionary where the key is the stock name and value is the df
    #this allows for easy access
    for name in csv_names:
        df = pd.read_csv(filepath+name)
        csv_files[df.Name.iloc[0]] = df
    return csv_files

def feature_extraction(csv_files):
    #extract features to allow easy access of the standard deviation (measure of risk) and latest price of the stock
    for stock in csv_files.values():
        std_dev = stock.close.std()
        name = stock.Name.iloc[0]
        lastVal = stock.close.iloc[-1]
        dict = {'Name' : name,'StandDev':std_dev, 'LastClosingVal' : lastVal}
        ser = pd.Series(dict)
        new_row_df = pd.DataFrame(ser).transpose()
        features = pd.concat([features, new_row_df], ignore_index=True)
    features.to_csv('../clean_data/stocks_clean.csv')

def main():
    start = input("Ready to start the program? (input yes or no) ")
    while(start != "yes"):
        start = input("Ready to start the program? (input yes or no)")
    print('Starting the program!')
    start_time = time.time()
    print('Importing csv files into dataframes...')
    project_directory = os.path.dirname(os.path.abspath("src"))
    #stocks_directory = os.path.dirname(os.path.abspath(project_directory)) 
    csv_files = csv_loader(project_directory+'/individual_stocks_5yr/')
    print('Successfully imported all data in ',round(time.time()-start_time, 4),' seconds!\n')

    print('Extracting key features from the data for later analysis...')
    features = pd.DataFrame(columns = ['Name', 'StandDev', 'LastClosingVal'])
    start_time = time.time()
    
    print('Feature extraction complete in ',round(time.time()-start_time, 4),' seconds!\n')
    data_structure = input("Would you like to build an adjacency matrix or an adjacency list? (M or L)\n")
    
    if data_structure == 'M':
        print('Building a graph as adjacency matrix...')
        graph = GraphClass.AdjacencyMatrixGraph()
        start_time = time.time()
        GraphClass.build_graph(csv_files, graph)
        print('Successfully built an adjacency matrix in', round(time.time()-start_time, 4), ' seconds!\n')
    elif data_structure == 'L':
        print('Building a graph as adjacency list...')
        graph = GraphClass.AdjacencyListGraph()
        start_time = time.time()
        GraphClass.build_graph(csv_files, graph)
        print('Successfully built an adjacency list in', round(time.time()-start_time, 4), ' seconds!\n')

    clean_stck_data = pd.read_csv(project_directory+'/clean_data/stocks_clean.csv')
    budget = float(input("Budget (No spaces or commas):\n$"))
    stock = input("Pick a stock from which you'd like to draw correlations (Ex: AAPL):\n")
    num_stocks = int(input("How many stocks would you like to invest in?:\n"))
    div = input("What would you like to do? (invest or short):\n")
    risk = input("High or low risk investment strategy? (H or L):\n")

    stock_dict = {}
    risk_bool = False
    if risk == "H":
        risk_bool = True
    elif risk == "L":
        risk_bool = False
    if div == "short":
        stock_heap = Heaps.MaxHeap(int(num_stocks))
    elif div == "invest":
        stock_heap = Heaps.MinHeap(int(num_stocks))

    for stock, correlation in graph.adjacency[stock].items():
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
