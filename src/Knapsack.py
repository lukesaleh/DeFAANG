
def knapsack_with_stocks_and_names(stocks, budget):
    num_stocks = len(stocks)

    # Initialize a 2D list to store the maximum risk for each subproblem
    dp = [[0] * (int(budget) + 1) for _ in range(num_stocks + 1)]

    # Initialize a dictionary to store the chosen stocks and their quantities
    chosen_stocks = {}

    # Build the table in a bottom-up manner
    for i in range(1, num_stocks + 1):
        stock_name, (stock_price, stock_risk) = list(stocks.items())[i - 1]

        for w in range(int(budget) + 1):
            # Handle the initial cases when knapsack capacity is 0 or no items to choose from
            if i == 0 or w == 0:
                dp[i][w] = 0
            elif stock_price <= w:
                # Decide whether to include the current stock
                if stock_risk + dp[i - 1][w - int(stock_price)] > dp[i - 1][w]:
                    dp[i][w] = stock_risk + dp[i - 1][w - int(stock_price)]
                    chosen_stocks[w] = chosen_stocks.get(w - int(stock_price), {}).copy()
                    chosen_stocks[w][stock_name] = chosen_stocks[w].get(stock_name, 0) + 1
                else:
                    dp[i][w] = dp[i - 1][w]
            else:
                # If the current stock cannot fit, use the risk from the previous row
                dp[i][w] = dp[i - 1][w]

    # Retrieve the chosen stocks with their quantities
    result_stocks = chosen_stocks.get(int(budget), {})
    print("Optimal stock allocation for maximized risk(only buying full shares):")
    # Return the chosen stocks with their names and quantities
    return result_stocks

