from stock import Stock
from portfolio import Portfolio
from bank_account import Bank_Account
import sys
import pickle

# Game list = [bank_account, portfolio, filename]

def main():
    game_list = intro()

    print('\n--------------------------------------------------------------------')
    keep_playing = True

    while keep_playing:
        action = int(input('\nPick an action:'
                           '\n(1) Portfolio'
                           '\n(2) Bank Account'
                           '\n(8) Save Game'
                           '\n(9) Exit program'))
        if action == 1:
            game_list = portfolio_mode(game_list[0], game_list[1], game_list[2])
        elif action == 2:
            game_list[0] = bank_account_mode(game_list[0])
        elif action == 8:
            save_file(game_list)
        elif action == 9:
            sys.exit()

def new_game():
    game_list = []
    bank_account = Bank_Account()
    game_list.append(bank_account)
    portfolio = Portfolio()
    game_list.append(portfolio)
    file_name = input("Enter the file name: ")
    file_name = file_name + '.file'
    game_list.append(file_name)
    save_file(game_list)
    return game_list

def load_game():
    correct_input = False
    while not correct_input:
        option = int(input("Do you know the name of your file?"
                      "\n(1) Yes"
                      "\n(2) No (will use default)"
                      "\n(3) Exit"
                      "\n>>>  "))
        if option == 1:
            file_name = input("Enter the name of the file without extension [ex) portfolio]: ")
            file_name = file_name + '.file'
            game_list = load_file(file_name)
            return game_list
        elif option == 2:
            game_list = load_file('portfolio_game.file')
            return game_list
        elif option == 3:
            sys.exit()
        else:
            print("Incorrect input. Try Again")

def save_file(game_list):
    with open(game_list[2] , 'wb') as f:
        pickle.dump(game_list, f)

def load_file(file_name):
    with open(file_name, 'rb') as f:
        game_list = pickle.load(f)
        return game_list

def intro():
    print("Welcome to the portfolio manager."
          "\n(1) New Game"
          "\n(2) Load Game"
          "\n(3) Exit")

    correct_input = False

    while not correct_input:
        option = int(input("Choose: "))
        if option == 1:
            game_list = new_game()
            correct_input = True
        elif option == 2:
            game_list = load_game()
            correct_input = True
        elif option == 3:
            sys.exit()
        else:
            print("Incorrect input try again")

    return game_list

def portfolio_mode(bank_account, portfolio, filename):
    game_list = []
    bank_account = bank_account
    portfolio = portfolio
    filename = filename
    print('\nWelcome to the portfolio manager.'
          '\nWhat would you like to do?')
    action = int(input('(1) Check Portfolio'
                       '\n(2) Buy Stock'
                       '\n(3) Sell Stock'
                       '\n(4) Check Stock'
                       '\n(9) Exit Portfolio Manager'))
    correct_input = False
    while not correct_input:

        # CHECK PORTFOLIO - 1
        if action == 1:
            step_2 = int(input('\nPick an option'
                               '\n(1) Review Portfolio'
                               '\n(2) Check Money invested in Portfolio'
                               '\n(3) Check Money invested in a stock'
                               '\n(4) Back'))
            step2_correct_input = False
            while not step2_correct_input:
                # Review Portfolio
                if step_2 == 1:
                    portfolio.review_portfolio()
                    step2_correct_input = True
                # Check Money Invested in Portfolio
                elif step_2 == 2:
                    print('Total invested: ', portfolio.total_money_invested())
                    step2_correct_input = True
                # Check Money Invested in a stock
                elif step_2 == 3:
                    ticker = input("Enter a ticker: ")
                    print(f'Total invested in {ticker}: ', portfolio.money_invested_by_stock(ticker))
                    step2_correct_input = True
                elif step_2 == 4:
                    step2_correct_input = True
                # Bad Input
                else:
                    print("Incorrect Input.")
            correct_input = True

        # BUY STOCK - 2
        elif action == 2:
            print('Your account balance is $', bank_account.check_balance(), '\n')
            step2_correct_input = False
            while not step2_correct_input:
                buy_or_short = int(input('(1) Buy'
                                         '\n(2) Short'
                                         '\n(3) Do Not Buy'
                                         '\nPick an option:  '))
                if buy_or_short == 1:
                    ticker = input('Enter the ticker: ')
                    amount = int(input('Enter the quantity to purchase: '))
                    portfolio.buy_stock(ticker, bank_account, amount)
                    step2_correct_input = True
                elif buy_or_short == 2:
                    ticker = input('Enter the ticker: ')
                    amount = int(input('Enter the quantity to purchase: '))
                    portfolio.buy_short_stock(ticker, bank_account, amount)
                    step2_correct_input = True
                elif buy_or_short == 3:
                    step2_correct_input = True
                else:
                    print('Incorrect Input')
            correct_input = True

        # SELL STOCK - 3
        elif action == 3:
            print('Your account balance is $', bank_account.check_balance(), '\n')
            step2_correct_input = False
            while not step2_correct_input:
                buy_or_short = int(input('(1) Sell Buy Stock'
                                         '\n(2) Sell Short Stock'
                                         '\n(3) Do not sell'))
                if buy_or_short == 1:
                    ticker = input('Enter the ticker: ')
                    amount = int(input('Enter the quantity to purchase: '))
                    portfolio.sell_buy_stock(ticker, bank_account, amount)
                    step2_correct_input = True
                elif buy_or_short == 2:
                    ticker = input('Enter the ticker: ')
                    amount = int(input('Enter the quantity to purchase: '))
                    portfolio.sell_short_stock(ticker, bank_account, amount)
                    step2_correct_input = True
                elif buy_or_short == 3:
                    step2_correct_input = True
                else:
                    print('Incorrect Input')
            correct_input = True

        # CHECK STOCK - 4
        elif action == 4:
            ticker = input('Enter the stock ticker: ')
            tmp_stock = Stock(ticker)
            print(f'The current cost for {ticker} is $', tmp_stock.get_purchase_cost())
            correct_input = True

        # EXIT - 9
        elif action == 9:
            correct_input = True

        # Incorrect Input
        else:
            print('Incorrect Input')

    game_list.append(bank_account)
    game_list.append(portfolio)
    game_list.append(filename)
    return game_list

def bank_account_mode(bank_account):
    bank_account = bank_account
    print('\nWelcome to your bank account')

    correct_answer = False
    while not correct_answer:
        entry = int(input('What would you like to do?'
                      '\n(1) Check Balance'
                      '\n(2) Get Funds'
                      '\n(9) Exit'))
        if entry == 1:
            print('Balance: $', bank_account.check_balance())
            correct_answer = True
        elif entry == 2:
            if bank_account.get_funds():
                print('Successfully added $1000')
            correct_answer = True
        elif entry == 9:
            correct_answer = True
        else:
            print("Bad Input. Try again")

    return bank_account

main()



