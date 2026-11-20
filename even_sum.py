"""Add the even numbers from 1 through 50 with two kinds of loops."""

# A for loop makes the range of numbers easy to see.
for_total = 0
for number in range(1, 51):
    if number % 2 == 0:
        for_total += number

print(f"The sum of even numbers from 1 to 50 is {for_total}.")

# A while loop reaches the same result by updating its counter each time.
while_total = 0
number = 1
while number <= 50:
    if number % 2 == 0:
        while_total += number
    number += 1

print(f"The while loop result is {while_total}.")
print("Both loops give the same result. I find the for loop clearer for a fixed range.")
