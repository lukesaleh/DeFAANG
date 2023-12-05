import os
import pandas as pd
import time
import Knapsack
import GraphClass
import Heaps
import matplotlib.pyplot as plt

def amount_to_invest(stocks, risk, budget):
    # normalize the value of standard deviations for each of the stocks
    print("\nBudget allocation: ")
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

def percent_change(stock_df):
    indices = [i for i in range(len(stock_df.index)) if i %5 == 0 or i == stock_df.index[-1]]
    change = []
    for i in range(len(indices)-1):
        opening = indices[i]
        closing = indices[i+1]
        change.append((stock_df.close.iloc[closing] - stock_df.open.iloc[opening] / stock_df.open.iloc[opening]))
    return change

def feature_extraction(csv_files, directory):
    #extract features to allow easy access of the standard deviation (measure of risk) and latest price of the stock
    features = pd.DataFrame(columns = ['Name', 'StandDev', 'LastClosingVal'])
    for stock in csv_files.values():
        std_dev = stock.close.std()
        name = stock.Name.iloc[0]
        lastVal = stock.close.iloc[-1]
        dict = {'Name' : name,'StandDev':std_dev, 'LastClosingVal' : lastVal}
        ser = pd.Series(dict)
        new_row_df = pd.DataFrame(ser).transpose()
        features = pd.concat([features, new_row_df], ignore_index=True)
    features.to_csv(directory+'/clean_data/stocks_clean.csv')

def slow_print_color(text, color_code, delay=0.003):
    for line in text.splitlines():
        print(f'\033[{color_code}m', end='')  # Start color
        for char in line:
            print(char, end='', flush=True)
            time.sleep(delay)
        print('\033[0m')  # Reset color
        time.sleep(delay)

def print_art():
    print("\nWelcome to DeFAANG investment!")
    print('')

    # ASCII art text
    art_text1 = "     _                ______ ___    ___   _   _ _____ "
    art_text2 = "    | |               |  ___/ _ \\  / _ \\ | \\ | |  __ \\"
    art_text3 = "  __| | ___   ______  | |_ / /_\\ \\/ /_\\ \\|  \\| | |  \\/"
    art_text4 = " / _` |/ _ \\ |______| |  _||  _  ||  _  || . ` | | __ "
    art_text5 = "| (_| |  __/          | |  | | | || | | || |\\  | |\\ \\"
    art_text6 = " \__,_|\\___|          \\_|  \\_| |_/\\_| |_/\\_| \\_/\\____/"

    art_text7 = "\n\n"
    art_text8 = "           /^\\/^\\"
    art_text9 = "         _|__|  O|"
    art_text10 = "\\/     /~     \\_/ \\\\"
    art_text11 = " \\____|__________/  \\"
    art_text12 = "        \\_______      \\"
    art_text13 = "                `\\     \\                 \\\\"
    art_text14 = "                  |     |                  \\\\"
    art_text15 = "                 /      /                    \\\\"
    art_text16 = "               /     /                       \\\\"
    art_text17 = "             /      /                         \\ \\"
    art_text18 = "            /     /                            \\  \\"
    art_text19 = "         /     /             _----_            \\   \\"
    art_text20 = "        /     /           _-~      ~-_         |   |"
    art_text21 = "       (      (        _-~    _--_    ~-_     _/   |"
    art_text22 = "        \\      ~-____-~    _-~    ~-_    ~-_-~    /"
    art_text23 = "          ~-_           _-~          ~-_       _-~"
    art_text24 = "             ~--______-~                ~-___-~"
    art_text25 = "\n(art from ASCII Art Archive)\n"

    # Slow-print each line with a delay between lines
    slow_print_color(art_text1, '36')  # Cyan color
    slow_print_color(art_text2, '36')
    slow_print_color(art_text3, '36')
    slow_print_color(art_text4, '36')
    slow_print_color(art_text5, '36')
    slow_print_color(art_text6, '36')
    slow_print_color(art_text7, '36')
    slow_print_color(art_text8, '33')  # Yellow color
    slow_print_color(art_text9, '33')
    slow_print_color(art_text10, '33')
    slow_print_color(art_text11, '33')
    slow_print_color(art_text12, '33')
    slow_print_color(art_text13, '33')
    slow_print_color(art_text14, '33')
    slow_print_color(art_text15, '33')
    slow_print_color(art_text16, '33')
    slow_print_color(art_text17, '33')
    slow_print_color(art_text18, '33')
    slow_print_color(art_text19, '33')
    slow_print_color(art_text20, '33')
    slow_print_color(art_text21, '33')
    slow_print_color(art_text22, '33')
    slow_print_color(art_text23, '33')
    slow_print_color(art_text24, '33')
    slow_print_color(art_text25, '33')

def main():
    start = input("Ready to start the program? (input yes or no) ")
    while(start != "yes"):
        start = input("Ready to start the program? (input yes or no) ")
    print('Starting the program!')
    start_time = time.time()
    print('Importing csv files into dataframes...')
    project_directory = os.path.dirname(os.path.abspath("src"))
    #stocks_directory = os.path.dirname(os.path.abspath(project_directory)) 
    csv_files = csv_loader(project_directory+'/individual_stocks_5yr/')
    print('Successfully imported all data in ',round(time.time()-start_time, 4),' seconds!\n')
    print('Extracting key features from the data for later analysis...')
    start_time = time.time()
    feature_extraction(csv_files, project_directory)
    print('Feature extraction complete in ',round(time.time()-start_time, 4),' seconds!\n')
    repeat = True
    while(repeat):
        print_art()

        print("\nYou will choose a stock from the S&P 500 and a few investment strategies.")
        print("We will allocate your budget in the most optimal way possible,")
        print("and optimize some stocks you may be able to pick if you want to maximize risk.\n")
        data_structure = input("Would you like to build an adjacency matrix or an adjacency list? (M or L)\n")
        while data_structure != "M" and data_structure != 'L':
            data_structure = input("Please input M or L\n")

        if data_structure == 'M':
            print('Building a graph as an adjacency matrix...')
            graph = GraphClass.AdjacencyMatrixGraph()
            start_time = time.time()
            GraphClass.build_graph(csv_files, graph)  # Assuming csv_files is defined
            print('Successfully built an adjacency matrix in', round(time.time() - start_time, 4), ' seconds!\n')
        elif data_structure == 'L':
            print('Building a graph as an adjacency list...')
            graph = GraphClass.AdjacencyListGraph()
            start_time = time.time()
            GraphClass.build_graph(csv_files, graph)  # Assuming csv_files is defined
            print('Successfully built an adjacency list in', round(time.time() - start_time, 4), ' seconds!\n')

        clean_stck_data = pd.read_csv(
            project_directory + '/clean_data/stocks_clean.csv')  # Assuming project_directory is defined
        budget = input("Budget (Only integers, no commas or spaces):\n$")
        while not budget.isdigit():
            budget = input("Budget (Only integers, no commas or spaces):\n$")
        budget = int(budget)

        stock = input("Pick a stock (S&P 500) from which you'd like to draw correlations (Ex: AAPL):\n")
        stock_a = stock
        num_stocks = input("How many stocks would you like to invest in? (integer):\n")
        while not num_stocks.isdigit():
            num_stocks = input("How many stocks would you like to invest in? (integer):\n")
        num_stocks = int(num_stocks)

        div = input("What would you like to do? (invest or short):\n")
        while div != "invest" and div != "short":
            div = input("Please input 'invest' or 'short': ")

        risk = input("High or low-risk investment strategy? (H or L):\n")
        while risk != "H" and risk != "L":  # Fixed the typo in the condition
            risk = input("Please input 'H' or 'L': ")

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

        for correlated_stock, correlation in graph.adjacency[stock].items():
            stock_heap.insert((correlation, correlated_stock))

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
        print('\nWould you like to explore the weekly percent change of a stock from your given portfolio (from 2013-2018)?')
        user_input = input('Type "yes" if you would like to explore these plots, else type any other word:\n').lower()
        
        while user_input == "yes":
            print('\nThe original stock you selected was',stock_a)
            stock_b = input('Tell us the stock from your portfolio you would like to compare against the original stock:')
            while stock_b not in stock_dict.keys():
                print('This stock was not in your portfolio')
                stock_b = input('Tell us the stock from your portfolio you would like to compare this stock to: ')
            plt.plot(percent_change(csv_files[stock_a]), color = 'red', label = stock_a)
            plt.plot(percent_change(csv_files[stock_b]), color = 'blue', label = stock_b)
            plt.xlabel('Week number')
            plt.ylabel('Percent change')
            plt.legend()
            plt.show()
            print('\nWould you like to explore the weekly percent change of another stock from your given portfolio (from 2013-2018)?')
            user_input = input('Type "yes" if you would like to explore these plots, else type any other word\n').lower()
        while(True):
            user_input = input('Would you like to repeat the program? Type "yes" or "no"\n').lower()
            if user_input == "yes" or user_input == "no":
                break
            else:
                print("Invalid input")
        repeat = True if user_input == "yes" else False
    print('\nThanks for investing with De-FAANG!')
# Implements the main
if __name__ == "__main__":
    main()
