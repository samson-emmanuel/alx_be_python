import sys
from bank_account import BankAccount

def main():
    account = BankAccount()

    if len(sys.argv) < 2:
        print("Usage: python main.py <command>:<amount>")
        print("Commands: deposit, withdraw, display")
        sys.exit(1)

    command, *params = sys.argv[1].split(':')

    if command == "deposit":
        if params:
            amount = float(params[0])
            account.deposit(amount)
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Usage: python main.py deposit:<amount>")

    elif command == "withdraw":
        if params:
            amount = float(params[0])
            success = account.withdraw(amount)
            if success:
                print(f'Withdrew: ${amount:.2f}')
            else:
                print("Insufficient funds.")
        else:
            print("Usage: python main.py withdraw:<amount>")

    elif command == "display":
        bal = account.get_balance()
        print(f"Current Balance: ${bal:.2f}")

    else:
        print("Invalid command.")

if __name__ == "__main__":
    main()
