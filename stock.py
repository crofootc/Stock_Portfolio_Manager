import datetime
import stock_functions as sf

class Stock:
    def __init__(self, ticker, status='buy'):
        self.__ticker = ticker
        self.__purchase_date = datetime.datetime.now()
        self.__purchase_cost = sf.get_stock_live_price(ticker)
        self.__status = status

    def get_ticker(self):
        return self.__ticker

    def get_purchase_date(self):
        return self.__purchase_date

    def get_purchase_cost(self):
        return float(self.__purchase_cost)

    def sell_stock(self):
        return float(sf.get_stock_live_price(self.__ticker))

