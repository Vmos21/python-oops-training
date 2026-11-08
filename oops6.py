class BankAccount:
    def __init__(self):
        self._balance = 0
    @property
    def balance(self):
        return self._balance
    def deposit(self, amt):
        self._balance += amt
    def withdraw(self, amt):
        if (self._balance < amt):
            print("ValueError: Insufficient funds")
        else:
            self._balance -= amt

acc = BankAccount()
acc.deposit(1000)
acc.withdraw(300)
print(acc.balance)
acc.withdraw(900)