def profit(arr):
    # Check length
    if len(stock_prices) < 2:
        raise Exception('Need at least two stock prices!')
    
    # Start minimum price marker at first price
    min_stock_price = stock_prices[0]
    
    # Start off with an initial max profit
    max_profit = stock_prices[1] - stock_prices[0]
    
    # Skip first index of 0
    for price in stock_prices[1:]:

        comparison_profit = price - min_stock_price

        max_profit = max(max_profit,comparison_profit)

        min_stock_price = min(min_stock_price,price)
        
    return max_profit

prices = [12,3,11,15,10]
print profit(prices)
