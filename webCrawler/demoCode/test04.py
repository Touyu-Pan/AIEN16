import munch

stocks = [{
    'code': 3001,
    'close': 128
}, {
    'code': 3012,
    'close': 54
}]
stocks = munch.munchify(stocks)

new_stocks = [
    f'{stock.close - 100}'
    for stock in stocks
    if stock.close >= 100
]
print(new_stocks)