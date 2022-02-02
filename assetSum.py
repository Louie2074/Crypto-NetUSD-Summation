'''
    File name: test.py
    Author: Louis Nguyen
    Python Version: 3
'''

import warnings
import pandas as pd
import sys
from ast import literal_eval
import json

cmdArgs = len(sys.argv)
assets = []
xlsx = False

#Makes sure that arguments are properly inputted
if cmdArgs != 4:
    raise Exception("Invalid number of arguments")
if sys.argv[1].endswith('.xlsx'):
    xlsx = True
if sys.argv[2].endswith('.txt'):
    text_file = open(f'./{sys.argv[2]}', 'r')
    data = text_file.read()
    text_file.close()
    assets = literal_eval(data)
if sys.argv[2].endswith('.json'):
    json_file = open('./test.json')
    data = json.load(json_file)
    json_file.close()
    assets = data

class Coin:
    def __init__(self, name, net, bought, sold):
        self.name = name
        self.net = net
        self.bought = bought
        self.sold = sold

#sets column data for gemini .xlsx files
def gemini():
    return ['Type', 'Symbol', 'USD Amount USD', 'Fee (USD) USD']

#sets column data for binance .csv files
def binance():
    return ['Operation', 'Base_Asset', 'Realized_Amount_For_Base_Asset_In_USD_Value', 'Realized_Amount_For_Fee_Asset_In_USD_Value']

#sets column data for coinbase .csv files
def cb():
    return ['Transaction Type', 'Asset', 'Subtotal', 'Fees']

#returns data frame to be parsed
def dataSetup(getData):
    data = []
    with warnings.catch_warnings(record=True):
        warnings.simplefilter("always")
        if xlsx:
            data = pd.read_excel(f'./{sys.argv[1]}')
        else:
            data = pd.read_csv(f'./{sys.argv[1]}')
    df = pd.DataFrame(data, columns=getData)
    return df

#parses dataframe and calculates sums and differences
def calculate(labels, sym):
    sum = 0
    diff = 0
    for index, row in labels.iterrows():
        if (row[0] == 'Buy' or row[0] == 'Sell') and row[1] == sym:
            diff += row[3]
            if row[0] == 'Buy':
                sum += abs(row[2])
            elif row[0] == 'Sell':
                diff += row[2]
    return Coin(sym, abs(sum-diff), sum, diff)


#calls calculate() on input names
def tabulate(function):
    output = []
    for sym in assets:
        output.append(calculate(function, sym))
    return output

#prints coins to terminal
def printCoins(coin):
    print('==============')
    print(f'{coin.name}')
    print(f'Net: ${coin.net}')
    print(f'Total Bought: ${coin.bought}')
    print(f'Total Sold: ${coin.sold}')


def init():
    inputF = None
    if int(sys.argv[3]) == 0:
        inputF = gemini()
    elif int(sys.argv[3]) == 1:
        inputF = binance()
    elif int(sys.argv[3]) == 2:
        inputF = cb()
    elif int(sys.argv[3]) == 3:
        inputF = binance()
    for coin in tabulate(dataSetup(inputF)):
        printCoins(coin)


init()
