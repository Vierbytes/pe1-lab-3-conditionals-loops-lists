"""Show common operations for working with a list."""

numbers = [64, 25, 12, 22, 11]
print(f"Original list: {numbers}")

# sorted() returns a new list and leaves numbers in its original order.
sorted_numbers = sorted(numbers)
print(f"Sorted copy: {sorted_numbers}")
print(f"Original list is unchanged: {numbers}")

# sort() changes the list in place.
numbers.sort()
print(f"After sort(): {numbers}")

numbers.append(30)
print(f"After appending 30: {numbers}")

numbers.remove(25)
print(f"After removing 25: {numbers}")

numbers.reverse()
print(f"After reverse(): {numbers}")
