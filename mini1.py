# Mini-Assignment 1
# class BankAccount
class BankAccount(object):

    # 1. constructor that only takes owner and balance values
    def __init__(self, owner, balance):
        if len(owner) > 10 and not str:
            raise ValueError("owner can only contain 10 characters and must be a string")
        if balance < 0:
            raise ValueError("should not be negative number")

        self.owner = str(owner)
        self.balance = float(balance)
        self.transactions = []

    # 2. toString that states only the owner and balance
    def __str__(self):
        return str(f"Owner: {self.owner} \n Balance: {self.balance}")

    # 3. deposit, add amount and print warning message
    def deposit(self, amount, transactions):
        self.balance + amount
        self.amount = float(100)
        transactions.append(f"Deposited: {self.amount}")
        if amount < 1:
            return f"Warning amount deposited, {self.amount} is less than one dollar!"

    # 4. withdraw, subtract the sp amt from balance, if insufficient funds print warning.
    def withdraw(self, amount):
        self.amount = float(50)
        self.balance -= amount
        if self.balance < amount:
            print("Warning! Insufficient funds!!!")

        self.transactions.append(f"Withdrew: {self.amount}")

    # 5. print current balance
    def display_balance(self):
        print(f"Balance: {self.balance}")

    # 6. prints all transaction for the account
    def display_transactions(self, transactions):
        for idx, transactions in enumerate(transactions):
            print(f"{idx}) {transactions}")


# Calling
#o1 = BankAccount('Lorena', 2500) #[100, 50])
#oss = o1.display_balance()
#tra = o1.display_transactions(0)
#print(oss, tra)
