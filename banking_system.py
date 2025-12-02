import sys
import time

def smooth_flow(text, delay=0.05):
    """Prints each character of the text with a specified delay."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def show_balance(balance):
    print("-------------------------")
    print(f"Your Balance is = {balance:,.2f}")

def deposit(balance):
    print("-------------------------")
    amount = float(input("Enter your amount you want to deposit: "))

    if amount <= 0:
        print("-------------------------")
        print("Amount can't be zero or less then zero.")
        return 0

    else:
        print("-------------------------")
        print(f"{amount:,.2f} rupees is deposit from your bank account.")
        return amount

def withdrawal(balance):
    print("-------------------------")
    amount = float(input("Enter amount you want to withdrawal: "))
    

    if amount > balance:
        print("-------------------------")
        print(f"Your Balance currently is = {balance:,.2f}")
        print("So, Amount cant zero or less then zero.")
        return 0

    else:
        print("-------------------------")
        print(f"{amount:,.2f} rupees is withdrawal from your bank account.")
        return amount



def main():
    balance = 0
    is_runnning = True

    while is_runnning:
        print("-------------------------")
        
        smooth_flow("Welcome to the Banking System", delay=0.02)
        smooth_flow("1. Check Balance", delay=0.02)
        smooth_flow("2. Deposit", delay=0.02)
        smooth_flow("3. Withdrawal", delay=0.02)
        smooth_flow("4. Exit", delay=0.02)

        smooth_flow("-------------------------", delay=0.02)

        choice = int(input("Enter your choice: "))

        if choice == 1:
            show_balance(balance)

        elif choice == 2:
            balance += deposit(balance)

        elif choice == 3:
            balance -= withdrawal(balance)

        elif choice == 4:
            print("Thank Q for visiting")
            is_runnning == False

        else:
            print("Invalid Input")

    print("Have a nice day")


if __name__ == "__main__":
    main()