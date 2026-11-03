
class BankAccount:
    bank_name = "Indian Bank"

    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
        self.transactions = ["Account Created"]

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            self.transactions.append(
                f"Deposited: Rs.{amount}"
            )
            print("Amount deposited successfully!")
        else:
            print("Enter a valid amount.")

    def withdraw(self, amount):
        if amount <= 0:
            print("Enter a valid amount.")
        elif amount <= self.__balance:
            self.__balance -= amount
            self.transactions.append(
                f"Withdrawn: Rs.{amount}"
            )
            print("Withdrawal successful!")
        else:
            print("Insufficient balance!")

    def check_balance(self):
        print("Current Balance: Rs.", self.__balance)

    def transaction_history(self):
        print("\n--- Transaction History ---")
        for transaction in self.transactions:
            print(transaction)


class SavingsAccount(BankAccount):
    def account_type(self):
        return "Savings Account"


class BankingSystem:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        name = input("Enter Account Holder Name: ")
        account_number = input("Enter Account Number: ")

        if account_number in self.accounts:
            print("Account already exists!")
            return

        account = SavingsAccount(name, account_number)
        self.accounts[account_number] = account
        print("Account created successfully!")

    def access_account(self):
        account_number = input("Enter Account Number: ")

        account = self.accounts.get(account_number)

        if account is None:
            print("Account not found!")
            return

        while True:
            print("\n--- Account Menu ---")
            print("1. Deposit")
            print("2. Withdraw")
            print("3. Check Balance")
            print("4. Transaction History")
            print("5. Back to Main Menu")

            choice = input("Enter your choice: ")

            if choice == "1":
                amount = float(input("Enter amount: Rs."))
                account.deposit(amount)

            elif choice == "2":
                amount = float(input("Enter amount: Rs."))
                account.withdraw(amount)

            elif choice == "3":
                account.check_balance()

            elif choice == "4":
                account.transaction_history()

            elif choice == "5":
                break

            else:
                print("Invalid choice!")


def main():
    bank = BankingSystem()

    while True:
        print("\n===== PYTHON BANKING SYSTEM =====")
        print("1. Create Account")
        print("2. Access Account")
        print("3. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bank.create_account()

        elif choice == "2":
            bank.access_account()

        elif choice == "3":
            print("Thank you for using Karthika Bank!")
            break

        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
