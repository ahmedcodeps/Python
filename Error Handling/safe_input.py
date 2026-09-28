def divide(num1, num2):
    return num1 + num2

def divide_numbers(num1, num2):
    if num1 == 0 or num2 == 0:
        print("Cannot divide by 0!")
        return
    try:
        num1 / num2
    except ZeroDivisionError:
        print("Cannot divide by 0!")
        return

    try:
        num1 / num2
    except ValueError:
        print("One of the values is wrong!")
        return

    return num1 / num2

n1 = input("Give any number: ")
n2 = input("Give a second number: ")

n1 = int(n1)
n2 = int(n2)

divide_numbers(n1, n2)