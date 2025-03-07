import math
import random

class Account:
    def __init__(self, account_number: int, customer_name: str, customer_address: str, balance: float):
        self.account_number = account_number
        self.customer_name = customer_name
        self.customer_address = customer_address
        self._balance = balance  # Приватное поле для инкапсуляции

    @property
    def balance(self) -> float:
        return self._balance

    def deposit(self, amount: float):
        if amount > 0:
            self._balance += amount
        else:
            raise ValueError("Deposit amount must be positive")

    def withdraw(self, amount: float):
        if amount > 0:
            if amount <= self._balance:
                self._balance -= amount
            else:
                raise ValueError("Insufficient funds")
        else:
            raise ValueError("Withdrawal amount must be positive")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, customer_name: str, customer_address: str, initial_balance: float) -> Account:
        account_number = self._generate_unique_account_number()
        account = Account(account_number, customer_name, customer_address, initial_balance)
        self.accounts[account_number] = account
        return account

    def get_account(self, account_number: int) -> Account:
        if account_number in self.accounts:
            return self.accounts[account_number]
        raise ValueError("Account not found")

    def _generate_unique_account_number(self) -> int:
        while True:
            account_number = math.floor(random.random() * 1000000)
            if account_number not in self.accounts:
                return account_number


class Customer:
    def __init__(self, name: str, address: str, bank: Bank):
        self.name = name
        self.address = address
        self.bank = bank

    def open_account(self, initial_balance: float) -> Account:
        return self.bank.create_account(self.name, self.address, initial_balance)


def banking_scenario():
    bank = Bank()
    customer1 = Customer("Alice", "Moscow, Stremyannyi per, 1", bank)
    customer2 = Customer("Bob", "Vorkuta, ul. Lenina, 5", bank)

    # Alice opens an account and deposits some money
    alice_account = customer1.open_account(initial_balance=500.0)
    alice_account.deposit(100.0)
    print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 600.0

    # Bob opens an account and deposits some money
    bob_account = customer2.open_account(initial_balance=1000.0)
    bob_account.deposit(500.0)
    print(f"Bob's balance: {bob_account.balance}")  # Bob's balance: 1500.0

    # Alice withdraws some money from her account
    alice_account.withdraw(300.0)
    print(f"Alice's balance: {alice_account.balance}")  # Alice's balance: 300.0

    # Alice tries to withdraw more money than she has
    try:
        alice_account.withdraw(500.0)
    except ValueError as e:
        print(e)  # Insufficient funds

    # Bank retrieves Alice's account using the account number
    retrieved_account = bank.get_account(alice_account.account_number)
    print(f"Account {retrieved_account.account_number} by {retrieved_account.customer_name} "
          f"({retrieved_account.customer_address}), balance {retrieved_account.balance}")


if __name__ == "__main__":
    banking_scenario()
