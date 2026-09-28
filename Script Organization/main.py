from file_manager import save_expense, load_expenses
from expenses import total_expenses


def main():
    while True:
        print("\nExpense Tracker")
        print("1. Add expense")
        print("2. View expenses")
        print("3. View total")
        print("4. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            description = input("Enter expense description: ")
            amount = float(input("Enter amount: "))

            save_expense(description, amount)
            print("Expense added.")

        elif choice == "2":
            expenses = load_expenses()

            if not expenses:
                print("No expenses found.")
            else:
                for description, amount in expenses:
                    print(f"{description}: ${amount:.2f}")

        elif choice == "3":
            expenses = load_expenses()
            total = total_expenses(expenses)

            print(f"Total expenses: ${total:.2f}")

        elif choice == "4":
            print("Goodbye!")
            break

        else:
            print("Invalid choice.")


if __name__ == "__main__":
    main()