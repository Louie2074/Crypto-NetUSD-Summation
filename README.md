# Crypto-NetUSD-Summation
This Tool parses csv and xlsx files for binance, coinbase (Regular) and gemini statement reports and prints out the Net amount of USD that you have spent per asset

# Instructions

To run the program, enter:

python3 assetSum.py <DATAFILE> <ASSETLIST> <INT>

The program takes 3 arguments, the first argument must be a valid csv or xlsx report from either gemini, coinbase or binance. The second argument must either be a 
text or json file that contains an array of Ticker Symbols (Ex. ["BTCUSD","ETHUSD"]). The third and final argument is an integer that specifies which 
exchange you which to perform the operation on. (0 = Gemini, 1 = Binance, 2 = Coinbase)
