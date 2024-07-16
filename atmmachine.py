# ATM Machine project in Python

# Dictionary to hold account number as key and tuple of (pin, balance) as value
accounts = {
    '123456': ('1234', 500),
    '987654': ('5678', 1000),
    # Add more accounts as needed
}

# Function to check if the account number exists
def is_valid_account(account_number):
    return account_number in accounts

# Function to check if the PIN is correct
def is_valid_pin(account_number, pin):
    if is_valid_account(account_number):
        return accounts[account_number][0] == pin
    return False

# Function to display the ATM menu
def display_menu():
    print("Welcome to the ATM Machine")
    print("1. Check Balance")
    print("2. Withdraw Money")
    print("3. Deposit Money")
    print("4. Quit")

# Function to check account balance
def check_balance(account_number):
    return accounts[account_number][1]

# Function to withdraw money
def withdraw_money(account_number, amount):
    current_balance = accounts[account_number][1]
    if amount > current_balance:
        print("Insufficient balance")
    else:
        accounts[account_number] = (accounts[account_number][0], current_balance - amount)
        print(f"Withdrawn {amount}. Current balance is {accounts[account_number][1]}")

# Function to deposit money
def deposit_money(account_number, amount):
    current_balance = accounts[account_number][1]
    accounts[account_number] = (accounts[account_number][0], current_balance + amount)
    print(f"Deposited {amount}. Current balance is {accounts[account_number][1]}")

# Main function to run the ATM
def main():
    print("Welcome to the ATM")
    while True:
        account_number = input("Enter your account number: ")
        pin = input("Enter your PIN: ")

        if is_valid_pin(account_number, pin):
            print("Login successful")
            while True:
                display_menu()
                choice = input("Enter your choice (1-4): ")
                if choice == '1':
                    print(f"Your balance is {check_balance(account_number)}")
                elif choice == '2':
                    amount = float(input("Enter amount to withdraw: "))
                    withdraw_money(account_number, amount)
                elif choice == '3':
                    amount = float(input("Enter amount to deposit: "))
                    deposit_money(account_number, amount)
                elif choice == '4':
                    print("Thank you for using the ATM. Goodbye!")
                    break
                else:
                    print("Invalid choice. Please enter a number between 1-4.")
        else:
            print("Invalid account number or PIN. Please try again.")

if __name__ == "__main__":
    main()
