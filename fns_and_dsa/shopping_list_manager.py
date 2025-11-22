shopping_list = []


def add_item(item):
    shopping_list.append(item)
    print(f'Item added: {item}')

def remove_item(item):
    if item not in shopping_list:
        print( f'Item "{item}" not found in the shopping list.')
    else:
        shopping_list.remove(item)
        print(f'Item "{item}" removed from the shopping list.')

def view_list():
    if not shopping_list:
        print("The shopping list is empty.")
    else:
        print("Shopping List:\n" + "\n".join(f"- {item}" for item in shopping_list))


def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == '1':
            # Prompt for and add an item
            item = input('Enter the item you want to add: ')
            add_item(item)

        elif choice == '2':
            # Prompt for and remove an item
            item = input('Enter the item you want to remove: ')
            remove_item(item)
            
        elif choice == '3':
            # Display the shopping list
            view_list()
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()