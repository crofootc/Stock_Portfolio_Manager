from datetime import datetime


class Bank_Account:
    def __init__(self):
        self.__start_date = datetime.now()
        self.__date_log = []
        self.__account = 0

    def get_funds(self):
        date = datetime.now()
        date = str(date.year) + ' ' + str(date.month) + ' ' + str(date.day)
        if date not in self.__date_log:
            self.__account += 1000
            self.__date_log.append(date)
            return True

        print("You have already collected your funds for the day.")
        return False

    def add_funds(self, amount):
        self.__account += amount

    def take_funds(self, amount):
        self.__account -= amount

    def check_balance(self):
        return self.__account


