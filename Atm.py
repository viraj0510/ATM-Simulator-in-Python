class ATM:
    def __init__(self, pin, balance=0):
        """Initialize ATM with a PIN and an optional starting balance."""
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def check_pin(self, pin):
        """Check if the entered PIN matches the stored PIN."""
        return self.pin == pin

    def inquire_balance(self):
        """Return the current balance."""
        return self.balance

    def withdraw_cash(self, amount):
        """Withdraw an amount from the balance if sufficient funds are available."""
        if amount > self.balance:
            return "Insufficient balance"
        self.balance -= amount
        self.transactions.append(f"Withdraw: -${amount}")
        return f"${amount} withdrawn. New balance: ${self.balance}"

    def deposit_cash(self, amount):
        """Deposit an amount to the balance."""
        self.balance += amount
        self.transactions.append(f"Deposit: +${amount}")
        return f"${amount} deposited. New balance: ${self.balance}"

    def change_pin(self, old_pin, new_pin):
        """Change the PIN if the old PIN is correct."""
        if not self.check_pin(old_pin):
            return "Invalid PIN"
        self.pin = new_pin
        return "PIN changed successfully"

    def get_transaction_history(self):
        """Return a list of transaction history."""
        if not self.transactions:
            return "No transactions found"
        return "\n".join(self.transactions)

def main():
    # Create an instance of ATM with a default PIN and balance
    atm = ATM(pin=1234, balance=500)

    # Loop to interact with the user until they choose to exit
    while True:
        print("\n--- ATM Menu ---")
        print("1. Balance Inquiry")
        print("2. Withdraw Cash")
        print("3. Deposit Cash")
        print("4. Change PIN")
        print("5. Transaction History")
        print("6. Exit")
        choice = input("Select an option: ")

        if choice == "1":
            # Balance Inquiry
            pin = int(input("Enter your PIN: "))
            if atm.check_pin(pin):
                print(f"Current balance: ${atm.inquire_balance()}")
            else:
                print("Incorrect PIN")

        elif choice == "2":
            # Withdraw Cash
            pin = int(input("Enter your PIN: "))
            if atm.check_pin(pin):
                amount = float(input("Enter amount to withdraw: "))
                print(atm.withdraw_cash(amount))
            else:
                print("Incorrect PIN")

        elif choice == "3":
            # Deposit Cash
            pin = int(input("Enter your PIN: "))
            if atm.check_pin(pin):
                amount = float(input("Enter amount to deposit: "))
                print(atm.deposit_cash(amount))
            else:
                print("Incorrect PIN")

        elif choice == "4":
            # Change PIN
            old_pin = int(input("Enter your old PIN: "))
            new_pin = int(input("Enter your new PIN: "))
            print(atm.change_pin(old_pin, new_pin))

        elif choice == "5":
            # Transaction History
            pin = int(input("Enter your PIN: "))
            if atm.check_pin(pin):
                print("Transaction History:")
                print(atm.get_transaction_history())
            else:
                print("Incorrect PIN")

        elif choice == "6":
            # Exit
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()
