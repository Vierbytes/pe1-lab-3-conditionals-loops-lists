"""Demonstrate logical and bitwise operations."""

def read_boolean(prompt):
    """Read true/false or 1/0 and return a Boolean value."""
    answer = input(prompt).strip().lower()
    return answer in ("true", "1", "yes", "y")


first_boolean = read_boolean("Enter the first value (true/false or 1/0): ")
second_boolean = read_boolean("Enter the second value (true/false or 1/0): ")

print(f"{first_boolean} and {second_boolean} = {first_boolean and second_boolean}")
print(f"{first_boolean} or {second_boolean} = {first_boolean or second_boolean}")
print(f"not {first_boolean} = {not first_boolean}")

first_number = 5
second_number = 3
print(f"{first_number} & {second_number} = {first_number & second_number} ({bin(first_number & second_number)})")
print(f"{first_number} | {second_number} = {first_number | second_number} ({bin(first_number | second_number)})")
print(f"{first_number} ^ {second_number} = {first_number ^ second_number} ({bin(first_number ^ second_number)})")
print(f"~{first_number} = {~first_number} ({bin(~first_number)})")
print(f"{first_number} << 1 = {first_number << 1} ({bin(first_number << 1)})")
print(f"{first_number} >> 1 = {first_number >> 1} ({bin(first_number >> 1)})")
