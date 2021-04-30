#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/bin/python3
import urllib.request
import json

GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# Enter your stock symbols here in the format: ["symbol1", "symbol2", ...]
stock_symbols = ['ADBE', 'PFPT', 'TSLA', 'AAPL', 'WMT']

api_url = 'https://query1.finance.yahoo.com/v7/finance/quote?'
fields = ['regularMarketPrice', 'regularMarketChange', 'regularMarketChangePercent']

with urllib.request.urlopen(f'{api_url}symbols={",".join(stock_symbols)}&fields={",".join(fields)}') as response:
    json_data = json.loads(response.read())

for stock_quote in json_data["quoteResponse"]["result"]:
    stock_symbol = stock_quote["symbol"]
    price_current = stock_quote["regularMarketPrice"]
    price_change = stock_quote["regularMarketChange"]
    price_change_percent = stock_quote["regularMarketChangePercent"]

    color = ''
    change = float(price_change)
    if change > 0:
        color = GREEN + '▲'

    if change < 0:
        color = RED + '▼'

    price_current = '{:.2f}'.format(price_current)
    price_change = color + '{:.2f}'.format(price_change) + RESET
    # price_change_percent = '(' + color + '{:.2f}%'.format(price_change_percent) + RESET + ')'

    print(f'{stock_symbol}  {price_current} {price_change}')
