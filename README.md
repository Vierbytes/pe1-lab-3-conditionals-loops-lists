# Lab 3: Conditionals, Loops, and Lists

This repository contains the grade checker, loop examples, list operations, a bubble sort walkthrough, and the optional logic and bitwise exercise.

## `grade_checker.py`

Example run with a grade of 84:

```text
Enter a grade from 0 to 100: 84
Your grade is: B
Nice work! Keep it up.
```

The program checks the boundaries from A through F and asks for a value in the 0–100 range.

## `even_sum.py`

```text
The sum of even numbers from 1 to 50 is 650.
The while loop result is 650.
Both loops give the same result. I find the for loop clearer for a fixed range.
```

## `list_operations.py`

```text
Original list: [64, 25, 12, 22, 11]
Sorted copy: [11, 12, 22, 25, 64]
Original list is unchanged: [64, 25, 12, 22, 11]
After sort(): [11, 12, 22, 25, 64]
After appending 30: [11, 12, 22, 25, 64, 30]
After removing 25: [11, 12, 22, 64, 30]
After reverse(): [30, 64, 22, 12, 11]
```

## `bubble_sort_demo.py`

```text
Starting list: [64, 25, 12, 22, 11]
After pass 1: [25, 12, 22, 11, 64]
After pass 2: [12, 22, 11, 25, 64]
After pass 3: [12, 11, 22, 25, 64]
After pass 4: [11, 12, 22, 25, 64]
Sorted list: [11, 12, 22, 25, 64]
```

The inner loop compares neighboring values. The outer loop repeats those comparisons until the largest unsorted value reaches the end.

## `logic_bits.py` (bonus)

This script asks for two Boolean values and prints `and`, `or`, and `not` results. It also prints binary representations for bitwise AND, OR, XOR, inversion, left shift, and right shift using the example integers 5 and 3.

Example with `true` and `false`:

```text
True and False = False
True or False = True
not True = False
5 & 3 = 1 (0b1)
5 | 3 = 7 (0b111)
5 ^ 3 = 6 (0b110)
~5 = -6 (-0b110)
5 << 1 = 10 (0b1010)
5 >> 1 = 2 (0b10)
```
