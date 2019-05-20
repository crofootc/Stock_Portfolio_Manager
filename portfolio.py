import stock

class Portfolio:
    def __init__(self):
        self.__portfolio = {}
        self.__portfolio_size = 0

    def buy_stock(self, ticker, bank_account, quantity=1):
            if ticker not in self.__portfolio:
                self.__portfolio[ticker] = {}
            if 'buy' not in self.__portfolio[ticker]:
                self.__portfolio[ticker]['buy'] = []
            new_stock = stock.Stock(ticker)
            for i in range(quantity):
                self.__portfolio[ticker]['buy'].append(new_stock)
                bank_account.take_funds((new_stock.get_purchase_cost()))

    def buy_short_stock(self, ticker, bank_account, quantity=1):
        if ticker not in self.__portfolio:
            self.__portfolio[ticker] = {}
        if 'short' not in self.__portfolio[ticker]:
            self.__portfolio[ticker]['short'] = []
        new_stock = stock.Stock(ticker, status='short')
        for i in range(quantity):
            self.__portfolio[ticker]['short'].append(new_stock)
            bank_account.take_funds(new_stock.get_purchase_cost())

    def get_stock_buy_total(self, ticker):
        if (ticker not in self.__portfolio) or ('buy' not in self.__portfolio[ticker]):
            return 0
        return len(self.__portfolio[ticker]['buy'])

    def sell_buy_stock(self, ticker, bank_account, quantity):
        if self.get_stock_buy_total(ticker) < quantity:
            print(f"There are not {quantity} {ticker} stocks in the portfolio")
            return 0

        amount_from_sale = 0
        # new_stock = stock.Stock(ticker)
        for i in range(quantity):
            tmp = (self.__portfolio[ticker]['buy']).pop()
            amount_from_sale += tmp.sell_stock()
        bank_account.add_funds(amount_from_sale)
        return amount_from_sale

    def sell_short_stock(self, ticker, bank_account, quantity):
        if self.get_stock_buy_total(ticker) < quantity:
            print(f"There are not {quantity} {ticker} stocks in the portfolio")
            return 0

        amount_from_sale = 0
        # new_stock = stock.Stock(ticker, status='short')
        for i in range(quantity):
            tmp = (self.__portfolio[ticker]['short']).pop()
            amount_from_sale += tmp.sell_stock()
            bank_account.add_funds((self.__portfolio[ticker]['buy'][len(self.__portfolio)-1].get_purchase_cost()))
        return amount_from_sale

    def review_portfolio(self):
        counter = 1
        for i in self.__portfolio:
            buy = 0
            short = 0
            if 'buy' in self.__portfolio[i]:
                buy = len(self.__portfolio[i]['buy'])
            if 'short' in self.__portfolio[i]:
                short = len(self.__portfolio[i]['short'])

            total = buy + short
            print(counter, ". ----------------------------")
            print("Ticker: ", i)
            print("Buy total: ", buy)
            print("Short total: ", short)
            print("Total: ", total)
            print()
            counter += 1

    def total_money_invested(self):
        total = 0
        for i in self.__portfolio:
            if 'buy' in self.__portfolio[i]:
                for j in range(len(self.__portfolio[i]['buy'])):
                    total += self.__portfolio[i]['buy'][j].get_purchase_cost()
            if 'short' in self.__portfolio[i]:
                for k in range(len(self.__portfolio[i]['short'])):
                    total += self.__portfolio[i]['short'][k].get_purchase_cost()
        return total

    def money_invested_by_stock(self, ticker):
        if ticker not in self.__portfolio:
            print("Not in Portfolio")
            return 0
        total = 0
        if 'buy' in self.__portfolio[ticker]:
            for i in range(len(self.__portfolio[ticker]['buy'])):
                total += self.__portfolio[ticker]['buy'][i].get_purchase_cost()
        if 'short' in self.__portfolio[ticker]:
            for i in range(len(self.__portfolio[ticker]['short'])):
                total += self.__portfolio[ticker]['short'][i].get_purchase_cost()

        return total
