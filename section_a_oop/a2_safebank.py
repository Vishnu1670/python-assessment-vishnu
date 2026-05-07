class BankAccount:

    def __init__(self, account_holder, initial_deposit):

        self.account_holder = account_holder
        #used the balance as a privet variable
        self.__balance = initial_deposit

        if initial_deposit < 500:
            raise ValueError("Initial deposit must be at least 500")
        
        #storing the transactions to a list
        self.transactions = []
        

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        # Add money
        self.__balance += amount
        # send the transaction details to the list
        self.transactions.append(
            f"DEPOSIT  +{amount}   Balance: {self.__balance}"
        )

    def withdraw(self, amount):
        if amount > self.__balance:
            raise ValueError("Insufficient balance")
        # Deduct money
        self.__balance -= amount
        # send the transaction details to the list
        self.transactions.append(
            f"WITHDRAW -{amount}   Balance: {self.__balance}"
        )

    def get_balance(self):
        return self.__balance

    def print_statement(self):
        print(f"Account Holder: {self.account_holder}")
        for index, transaction in enumerate(self.transactions, start=1):
            print(f"{index}. {transaction}")

        print(f"Current Balance: Rs.{self.__balance}")



acc = BankAccount("Arun Kumar", 1000)

acc.deposit(500)

acc.withdraw(300)

acc.print_statement()