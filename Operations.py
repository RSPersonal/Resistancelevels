import yfinance as yf


class Operations():
    """A class for all of the operations"""
    
    def get_info(self, ticker):
        stock = yf.Ticker(ticker)
        return stock.info