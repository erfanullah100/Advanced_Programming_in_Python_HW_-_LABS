from abc import ABC, abstractmethod

class Account(ABC):
    def __init__(self, account_number, balance):
        self.account_number = account_number
        self._balance = balance

    @property
    def balance(self):
        return self._balance

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    def withdraw(self, amount):
        if 0 < amount <= self._balance:
            self._balance -= amount

    @abstractmethod
    def calculate_interest_or_fees(self):
        pass

    def __str__(self):
        return f"Acc No: {self.account_number} | Balance: ${self._balance:.2f}"


class SavingsAccount(Account):
    def __init__(self, account_number, balance, interest_rate=0.03):
        super().__init__(account_number, balance)
        self.interest_rate = interest_rate

    def calculate_interest_or_fees(self):
        return self.balance * self.interest_rate


class CurrentAccount(Account):
    def __init__(self, account_number, balance, maintenance_fee=12.00):
        super().__init__(account_number, balance)
        self.maintenance_fee = maintenance_fee

    def calculate_interest_or_fees(self):
        return -self.maintenance_fee


if __name__ == "__main__":
    savings = SavingsAccount("SAV-101", 5000.00)
    current = CurrentAccount("CUR-202", 1500.00)

    savings.deposit(500.00)
    current.withdraw(200.00)

    accounts = [savings, current]

    for acc in accounts:
        adjustment = acc.calculate_interest_or_fees()
        label = "Interest Earned" if adjustment >= 0 else "Maintenance Fee"
        print(f"{acc} | {label}: ${abs(adjustment):.2f}")
