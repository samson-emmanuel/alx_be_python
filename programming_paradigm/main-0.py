import sys
from bank_account import BankAccount

def main():
    account = BankAccount()  # Start balance at 0 unless tests set it manually

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')

    if command == "deposit":
        if params:
            amount = float(params[0])
            account.deposit(amount)
        else:
            print("Usage: python main.py deposit:<amount>")
    elif command == "withdraw":
        if params:
            amount = float(params[0])
            if not account.withdraw(amount):
                print("Insufficient funds.")
        else:
            print("Usage: python main.py withdraw:<amount>")
    elif command == "display":
        account.display_balance()
    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
