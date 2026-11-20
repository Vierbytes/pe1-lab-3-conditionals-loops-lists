"""Sort a short list with bubble sort and show each pass."""

numbers = [64, 25, 12, 22, 11]
print(f"Starting list: {numbers}")

# Each outer pass moves the largest remaining value to the right.
for pass_number in range(len(numbers) - 1):
    # Compare adjacent values and swap them when they are out of order.
    for index in range(len(numbers) - 1 - pass_number):
        if numbers[index] > numbers[index + 1]:
            numbers[index], numbers[index + 1] = numbers[index + 1], numbers[index]

    print(f"After pass {pass_number + 1}: {numbers}")

print(f"Sorted list: {numbers}")
