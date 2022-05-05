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

account1 = BankAccount(0.05, 0)
account1.deposit(5000).display_account_info().yield_interest().display_account_info().withdraw(500).deposit(10000)

account2 = BankAccount(0.01, 100)
account2.deposit(50).display_account_info().yield_interest().display_account_info().withdraw(500).deposit(10000)
