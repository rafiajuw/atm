
class ATM:
    def __init__(self):
        """Initialize the ATM with default balance and PIN"""
        self.balance = 1000  
        self.pin = "1234"    
    
    def check_pin(self, input_pin):
        """Check if the entered PIN matches the default PIN"""
        return input_pin == self.pin
    
    def check_balance(self):
        """Return the current account balance"""
        return self.balance
    
    def deposit(self, amount, input_pin):
        """
        Deposit money into the account if PIN is correct
        and amount is positive
        """
        if not self.check_pin(input_pin):
            return "Incorrect PIN. Transaction cancelled."
        if amount <= 0:
            return "Invalid amount. Please enter a positive value."
        
        self.balance += amount
        return f"Deposit successful. New balance: ${self.balance}"
    
    def withdraw(self, amount, input_pin):
        """
        Withdraw money from the account if PIN is correct,
        amount is positive, and sufficient balance exists
        """
        if not self.check_pin(input_pin):
            return "Incorrect PIN. Transaction cancelled."
        if amount <= 0:
            return "Invalid amount. Please enter a positive value."
        if amount > self.balance:
            return "Insufficient funds. Transaction cancelled."
        
        self.balance -= amount
        return f"Withdrawal successful. New balance: ${self.balance}"
    
    @staticmethod
    def exit():
        """Exit the ATM system"""
        print("Thank you for using our ATM. Goodbye!")
        return None


def main():
    """Main function to run the ATM menu system"""
    atm = ATM()
    
    print("Welcome to ATM")
    
    # PIN verification loop
    verified = False
    attempts = 3
    
    while not verified and attempts > 0:
        input_pin = input("Enter your PIN: ")
        if atm.check_pin(input_pin):
            verified = True
        else:
            attempts -= 1
            if attempts > 0:
                print(f"Incorrect PIN. {attempts} attempts remaining.")
            else:
                print("Too many incorrect attempts. Card blocked.")
                return
    
    # Main menu loop
    while verified:
        print("\nPlease select an option:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Exit")
        
        choice = input("Enter your choice (1-4): ")
        
        if choice == "1":
            print(f"Your current balance is: ${atm.check_balance()}")
        elif choice == "2":
            try:
                amount = float(input("Enter deposit amount: $"))
            
                pin = input("Enter your PIN again: ")
                print(atm.deposit(amount, pin))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == "3":
            try:
                amount = float(input("Enter withdrawal amount: $"))
            
                pin = input("Enter your PIN again: ")
                print(atm.withdraw(amount, pin))
            except ValueError:
                print("Invalid amount. Please enter a numeric value.")
        elif choice == "4":
            atm.exit()
            break
        else:
            print("Invalid choice. Please select 1-4.")


if __name__ == "__main__":
    main()
