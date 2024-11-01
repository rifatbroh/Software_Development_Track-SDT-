"""
    suppose 5 banks in comilla region now make project
    for this bank
    here your including this process:
        -> class
        -> attribute
        -> constructor

        ... function
        -> get_balance
        -> deposite
        -> withdraw
        ->
"""

class Bank:
    def __init__(self, balance) -> None:
        self.balance = balance
        self.min_withdraw = 500
        self.max_withdraw = 50000

    def get_balance(self):
        return self.balance
    
    def deposite(self, amount):
        if amount > 0:
            self.balance += amount

    def withdraw(self, amount):
        if amount < self.min_withdraw:
            print(f'NO!, you can withdraw below {self.min_withdraw}')
        elif amount > self.max_withdraw:
            print(f'bhai bank e taka nai, you can not more than {self.max_withdraw}')
        else:
            self.balance -= amount
            print(f'Here is your money {amount}')
            print(f'Now your balance after withdraw {self.get_balance()}')



# define or declar object 
brac = Bank(25000)
brac.withdraw(400)
brac.withdraw(1000)

dbbl = Bank(5000)
dbbl.deposite(2000)
dbbl.deposite(2000)
dbbl.withdraw(1700)
print(dbbl.get_balance())