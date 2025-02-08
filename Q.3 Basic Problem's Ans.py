## Question: String Reverse: Write a Python function to reverse a given string and return the reversed string.
## Answer:


#Python function to reverse
def reverse_string(input_string):
    return input_string[::-1]

# Example usage
original_string = "Hello, World!"
reversed_string = reverse_string(original_string)
print(f"Original String: {original_string}")
print(f"Reversed String: {reversed_string}")
