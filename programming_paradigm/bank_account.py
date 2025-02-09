class BankAccount:

    def __init__(self,initial_balance=0.0):
        self.account_balance = initial_balance

    def deposit(self,amount):
        if amount > 0:
            self.account_balance =+ amount
        else: 
            return "account balance cannot be negative "

    def withdraw(self,amount):
        if amount<= 0:
            print( "withdrawn amount cannot be negative")
            return False
        elif amount > self.account_balance:
            print ("Insufficient funds")
            return False
        else: 
            self.account_balance =- amount 
            return True

    def display_balance():
        print(f"Current Balance: ${self.account_balance:.2f}")
