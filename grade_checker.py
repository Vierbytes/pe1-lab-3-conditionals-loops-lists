"""Convert a numeric grade to a letter grade."""

grade = int(input("Enter a grade from 0 to 100: "))

# Check the range first, then compare from the highest letter grade downward.
if grade < 0 or grade > 100:
    print("Please enter a grade from 0 to 100.")
else:
    if grade >= 90:
        letter_grade = "A"
    elif grade >= 80:
        letter_grade = "B"
    elif grade >= 70:
        letter_grade = "C"
    elif grade >= 60:
        letter_grade = "D"
    else:
        letter_grade = "F"

    print(f"Your grade is: {letter_grade}")
    message = "Nice work! Keep it up." if letter_grade in ("A", "B", "C") else "Keep practicing and try again."
    print(message)
