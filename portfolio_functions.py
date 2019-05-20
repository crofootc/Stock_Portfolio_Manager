import pickle

def save_portfolio(portfolio):
    with open('portfolio.file', 'wb') as f:
        pickle.dump(portfolio, f)


def load_portfolio():
    with open('portfolio.file', 'rb') as f:
        portfolio = pickle.load(f)
    return portfolio




