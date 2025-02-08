## Question 1: Variable Swap: Write a Python program to swap the values of two variables without using a temporary variable.
## Initial values
a = 5
b = 10
print(f"Before swapping: a = {a}, b = {b}")

## Swapping the values
a, b = b, a
print(f"after swapping: a = {a}, b = {b}")