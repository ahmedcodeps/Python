def total_expenses(expenses):
    total = 0

    for description, amount in expenses:
        total += amount

    return total