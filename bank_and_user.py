class BankAccount:
    def __init__(self, int_rate, balance):
        self.int_rate = int_rate
        self.balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
        else:
            print("You can't deposit a negative value")
        return self
    def withdraw(self, amount):
        if self.balance > amount:
            self.balance -= amount
            print(f"Your new balance is {self.balance}")
        else:
            self.balance -= 5
            print(f"You do not have enough funds to cover this transaction. We withdrew $5 as a fee. Your new balance is {self.balance}")
        return self
    def display_account_info(self):
        print("BALANCE: ", self.balance)
        return self
    def yield_interest(self):
        if self.balance > 0:
            self.balance = self.balance * (1 + self.int_rate)
        return self

class User:
    def __init__(self, first_name, last_name, email):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.checking_account = BankAccount(int_rate = 0.05, balance = 0)
    def make_deposit(self, amount):
        self.checking_account.deposit(amount)
    def make_withdrawl(self, amount):
        self.checking_account.withdraw(amount)
    def display_info(self):
        self.checking_account.display_account_info()

account1 = BankAccount(0.05, 0)
account1.deposit(5000).display_account_info().yield_interest()

account2 = BankAccount(0.01, 100)
account2.deposit(50).display_account_info().yield_interest()

user1 = User('John', 'Glass', 'john@glass.com')
user1.make_deposit(100)
user1.display_info()