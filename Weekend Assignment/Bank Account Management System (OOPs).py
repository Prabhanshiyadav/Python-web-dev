class BankAccount:
    def __init__(self, account_number, holder_name, balance):
        self.__account_number = account_number
        self.__holder_name = holder_name
        self.__balance = balance
    def get_account_number(self):
        return self.__account_number
    def get_holder_name(self):
        return self.__holder_name
    def get_balance(self):
        return self.__balance
    def set_holder_name(self, name):
        self.__holder_name = name
    def set_balance(self, balance):
        self.__balance = balance
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"₹{amount} deposited successfully.")
        else:
            print("Enter a valid deposit amount.")
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        elif amount <= 0:
            print("Enter a valid withdrawal amount.")
        else:
            self.__balance -= amount
            print(f"₹{amount} withdrawn successfully.")
    def display_account_info(self):
        print(f"Account Number : {self.__account_number}")
        print(f"Holder Name    : {self.__holder_name}")
        print(f"Balance        : ₹{self.__balance}")
if __name__ == "__main__":
    account = BankAccount("1234567890", "Prabhanshi Yadav", 5000)
    account.display_account_info()
    account.deposit(2000)
    account.withdraw(1000)
    account.withdraw(10000)
    account.display_account_info()
