import uuid

class Account:

    def __init__(self, id, amount=0):
        self.account_id = id
        self._account_amount = amount

    def deposit(self, depo_amt):
        if not isinstance(depo_amt, (int, float)):
            raise AttributeError
        self._account_amount += depo_amt

    def withdraw(self, withd_amt):
        if not isinstance(withd_amt, (int, float)):
            raise AttributeError
        self._account_amount -= withd_amt

    def transfer(self, account, amount):
        if not isinstance(account, Account):
            raise TypeError
        self._account_amount -= amount
        account._account_amount += amount

class CreditAccount(Account):

    def __init__(self, id, amount=0, interest_rate=0):
        super().__init__(id, amount)
        self.interest_rate = interest_rate

    def computer_interest(self):
        if self.account_amount < 0:
            self.account_amount = self.account_amount*(100+self.interest_rate) / 100

class SavingsAccount(Account):
    
    def __init__(self, id, amount=0):
        super().__init__(id, amount)

    @property
    def amount(self):
        return self._account_amount
    
    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("Savings account balance cannot be negative.")
        self._account_amount = value




jack = Account(uuid.uuid4(), 1500)
john = Account(uuid.uuid4(), 5000)
print(jack._account_amount, john._account_amount)

jack.transfer(john, 750)
print(jack._account_amount, john._account_amount)