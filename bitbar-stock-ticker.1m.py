#!/usr/bin/env PYTHONIOENCODING=UTF-8 /usr/bin/python3
import urllib.request
import json

GREEN = '\033[32m'
RED = '\033[31m'
RESET = '\033[0m'

# Enter your stock symbols here in the format: ["symbol1", "symbol2", ...]
stock_symbols = ['AAPL', 'ADBE', 'KO', 'WMT', 'BND', 'SPY']

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

    print(f'{stock_symbol:<6}{price_current:.2f} {color}{price_change:.2f} ({price_change_percent:.2f}%){RESET}')
