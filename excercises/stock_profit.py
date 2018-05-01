def profit(arr):
    if len(arr) == 1:
        return arr

    min_price = arr[0]
    max_profit = 0

    for value in arr[1:]:
        min_price = min(min_price,value)
        comp_profit = value - min_price
        max_profit = max(max_profit,comp_profit)
    return max_profit

prices = [12,3,11,15,10]
print profit(prices)
