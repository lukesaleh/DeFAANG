import os




def correlation_retriever(file_path1, file_path2):
    return 0.0

def stock_info(stock_dictionary):
    


    std_deviation = 0.0
    price = 0.0
    return std_deviation, price


def Graph_build(file_list):
    rows = cols = len(file_list)

    Adj_matrix = [[0] * cols for i in range(rows)]

    for index1, file1 in enumerate(file_list):
        for index2, file2 in enumerate(file_list):
            Adj_matrix[index1][index2] = correlation_retriever(file1, file2)
    
    return Adj_matrix
    

def main():
     # Assuming your_script.py is located in the source_directory
    project_directory = os.path.dirname(os.path.abspath("main.py"))  # Get the directory of the script

    # Construct the path to the "individual_stocks_5yr" directory
    stocks_directory = os.path.join(project_directory, 'individual_stocks_5yr')

    # Get a list of file names in the "individual_stocks_5yr" directory
    file_list = os.listdir(stocks_directory)

    stock_graph = Graph_build(file_list)
    stock_indices = {index: stock_name.replace('_data.csv', '') for index, stock_name in enumerate(file_list)}

# Implements the main
if __name__ == "__main__":
    main()


            