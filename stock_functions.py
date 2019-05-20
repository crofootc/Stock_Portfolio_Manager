import requests
from termcolor import colored
import pandas as pd


'''
The get_stock_dataframe function pulls stock data from alpha vantage and returns it as a panda dataframe
It takes two parameters, the ticker symbol and size
Size can either be full or compact but is defaulted to full
'''
def create_stock_dataframe(ticker="NONE", size="full"):
    if ticker == "NONE":
        return None

    function = 'function=TIME_SERIES_DAILY'
    symbol = f'symbol={ticker}'
    size = f'outputsize={size}'
    api_key = 'apikey=C0S1BTKMMN5286JT'
    url = f'https://www.alphavantage.co/query?&{function}&{symbol}&{size}&{api_key}'

    response = requests.get(url)
    json_stock_data = response.json()

    if 'Error Message' in json_stock_data:
        print(colored(f'Invalid API call for ticker {ticker}', 'red'))
        return None

    df = pd.DataFrame.from_dict(json_stock_data['Time Series (Daily)'], orient='index')

    return df


def get_stock_live_price(ticker="NONE"):
    if ticker == "NONE":
        return None

    function = 'function=GLOBAL_QUOTE'
    symbol = f'symbol={ticker}'
    api_key = 'apikey=C0S1BTKMMN5286JT'
    url = f'https://www.alphavantage.co/query?&{function}&{symbol}&{api_key}'


    response = requests.get(url)
    json_stock_data = response.json()

    return json_stock_data['Global Quote']['05. price']