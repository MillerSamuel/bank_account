class BankAccount:
    all_accounts=[]
    def __init__(self, int_rate, balance=0): 
        self.int_rate=int_rate
        self.balance=balance
        BankAccount.all_accounts.append(self)

    def deposit(self, amount):
        self.balance+=amount
        return self
    def withdraw(self, amount):
        if BankAccount.can_withdraw(self.balance,amount):
            self.balance-=amount
        else:
            print("Insufficient funds: Charging a $5 fee")
            self.balance-=5
        return self
    def display_account_info(self):
        print(f"Balance: {self.balance}  Interest Rate:{self.int_rate}")
        return self
    def yield_interest(self):
        self.balance*=(self.int_rate+1)
        return self
    @classmethod
    def display_all(cls):
        for i in BankAccount.all_accounts:
            print(f"Balance:{i.balance}  Interest Rate:{i.int_rate}")
    @staticmethod
    def can_withdraw(balance,amount):
        if (balance - amount) < 0:
            return False
        else:
            return True


account1=BankAccount(0.1,100)
account2=BankAccount(0.2,100)

account1.deposit(100).deposit(50).deposit(50).withdraw(100).yield_interest().display_account_info()
account2.deposit(100).deposit(150).withdraw(50).withdraw(50).withdraw(50).withdraw(50).yield_interest().display_account_info()
account2.withdraw(200)
BankAccount.display_all()