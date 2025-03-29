class Account:
    interest = 0.02
    def __init__(self,account_holder):
        self.balance = 0
        self.holder = account_holder
    def deposit(self,amount):
        self.balance = self.balance + amount
        return self.balance
    def withdraw(self,amount):
        if amount > self.balance:
            return '钱不够'
        else:
            self.balance = self.balance - amount
            return self.balance
class ChekingAccount(Account):
    interest = 0.01
    withdraw_fee = 1
    def withdraw(self, amount):
        return Account.withdraw(self,amount + self.withdraw_fee)
class Bank:
    """
    A bank *has* accounts.
    >>> bank = Bank()
    >>> john = bank.open_account('John',10)
    >>> jack = bank.open_account('Jack',5,ChekingAccount)
    
    """
