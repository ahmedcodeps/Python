
grade = input("Enter your grade: ")
grade = int(grade)

letter = 'A'

if grade >= 90:
    letter = 'A'
elif grade >= 80:
    letter = 'B'
elif grade >= 70:
    letter = 'C'
elif grade >= 60:
    letter = 'D'
elif grade < 60:
    letter = 'F'

if grade <= 0 or grade >= 100:
    print("Invalid grade.")
else:
    print(f"Your letter grade is {letter}.")
