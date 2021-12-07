stocks = {
    '3001': 128,
    '3012': 54
}

print(stocks.items())

new_stocks = [
    f'{close - 100}'
    for code, close in stocks.items()
    if close >= 100
]
print(new_stocks)