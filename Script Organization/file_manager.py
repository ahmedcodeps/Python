def save_expense(description, amount):
    with open("expenses.txt", "a") as file:
        file.write(f"{description},{amount}\n")


def load_expenses():
    expenses = []

    try:
        with open("expenses.txt", "r") as file:
            for line in file:
                description, amount = line.strip().split(",")
                expenses.append((description, float(amount)))
    except FileNotFoundError:
        pass

    return expenses