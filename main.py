import pandas as pd
import numpy as np
import yfinance
import matplotlib.dates as mpl_dates
import matplotlib.pyplot as plt
from Operations import Operations

Tickers = ['MSFT', 'AMZON' , 'AAPL']

def main():
    
    plt.rcParams['figure.figsize'] = [12, 7]
    plt.rc('font', size=14)
    
    for ticker in Tickers:
        print(Operations().get_info(ticker))

    

if __name__ == '__main__':
    main()