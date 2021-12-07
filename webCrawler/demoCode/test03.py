stocks = [12, 105, 268, 113, 12, 54]

# new_stocks = []
# for stock in stocks:
#     if stock >= 100:
#         new_stocks.append(stock)

new_stocks = [
    f'{stock - 100}'
    for stock in stocks
    if stock >= 100
]
print(new_stocks)