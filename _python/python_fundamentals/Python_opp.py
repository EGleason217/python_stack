class User:
    def __init__(self, username, email_address):
        self.name = username
        self.email = email_address
        self.account_balance = 0
    def make_deposit(self, amount):
        self.account_balance += amount
    def make_withdrawal(self,amount):
        self.account_balance -= amount
    def display_user_balance(self):
        print("User: " + self.name + " -- Account Balance: " + str(self.account_balance))
    def transfer(self, to_account, amount):
        to_account.make_deposit(amount)
        self.make_withdrawal(amount)

korine = User("Korine", "angelkorine@yahoo.com")
korim = User("Korim", "korim_powell@outlook.com")
davron = User("Davron", "davron_powell@outlook.com")

print(korine.name)
print(korim.name)

korine.make_deposit(1000)
print(korine.account_balance)

korine.make_deposit(2000)
print(korine.account_balance)

korine.make_withdrawal(333)
print(korine.account_balance)


korine.transfer(korim,600)
korine.display_user_balance()
korim.display_user_balance()