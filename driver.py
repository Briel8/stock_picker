def stock_picker(daily_stock_prices):
    final_buy = 0
    final_sell = 0
    profit = 0
    prices_after_buying = []
    for i in range(len(daily_stock_prices) -1):
        if daily_stock_prices[i] < daily_stock_prices[i + 1]:
            prices_after_buying = daily_stock_prices[i + 1 : len(daily_stock_prices)]
            buy = daily_stock_prices[i]
            sell = max(prices_after_buying)
            if sell - buy > profit:
                profit = sell - buy
                final_buy = buy
                final_sell = sell
    return [final_buy, final_sell]

print(stock_picker([3,6,9,15,8,6,1,10,17]))