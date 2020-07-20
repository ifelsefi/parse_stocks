#!/usr/bin/env python

import csv
from collections import Counter
exchanges = Counter()
tickers = Counter()

with open("stocks.csv") as file:
    stocks = csv.reader(file)
    if csv.Sniffer().has_header:
        next(stocks)
    for row in stocks:
        exchanges[row[2]] += 1
        tickers[row[1]] += 1

    print("NYSE trades: %s" % exchanges['NYSE'])
    print("NDAQ trades: %s" % exchanges['NDAQ'])
    print("TSX trades: %s" % exchanges['TSX'])
