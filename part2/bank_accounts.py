class BalanceException(Exception):
    pass


class BankAccount:
    def __init__(self, initialAmount, acctName):
        self.balance = initialAmount
        self.name = acctName
        print(f"Created account {self.name} with balance {self.balance}")
        
    def getBalance(self):
        print(f"Balance for account {self.name} is {self.balance}")

    def deposit(self, amount):
        self.balance = self.balance + amount
        print(f"Deposited {amount} into account {self.name}. New balance is {self.balance}")    
        self.getBalance()

    def vaiableTransaction(self, amount):
        if self.balance >= amount:
            return
        else:
            raise BalanceException(f"Insufficient funds in account {self.name} to withdraw {amount}. Balance is {self.balance}")
        
    def withdraw(self, amount):
        try:
            self.vaiableTransaction(amount)
            self.balance = self.balance - amount
            print(f"Withdrew {amount} from account {self.name}. New balance is {self.balance}")
            self.getBalance()
        except BalanceException as error:
            print("An exception occurred: ", {error})

    def transfer(self, amount, account):
        try:
            print('\n**********\nBeginning transfer...')
            self.vaiableTransaction(amount)
            self.withdraw(amount)
            account.deposit(amount)
            print('Transfer complete\n**********\n')
        except BalanceException as error:
            print("An exception occurred: ", {error})


class InterestRewardsAcct(BankAccount):
    def deposit(self, amount):
        self.balance = self.balance = (amount * 1.05)
        print(f"Deposited {amount} into account {self.name}. New balance is {self.balance}")
        self.getBalance()


class SavingsAcct(InterestRewardsAcct):
    def __init__(self, initialAmount, acctName):
        super().__init__(initialAmount, acctName)
        print(f"Created account {self.name} with balance {self.balance}")
        self.fee = 5

    def withdraw(self, amount):
        try:
            self.vaiableTransaction(amount = self.fee)
            self.balance = self.balance - (amount * self.fee)
            print(f"Withdrew {amount} from account {self.name}. New balance is {self.balance}")
        except BalanceException as error:
            print("An exception occurred: ", {error})