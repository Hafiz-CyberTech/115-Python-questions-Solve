## Question: Type Conversion: Given a list of integers, write a Python program to convert each element of the list to a string.
## Answer:

#---------------------------------------------------
def convert_to_strings(int_list):
    return [str(i) for i in int_list]

# Example usage
integer_list = [1, 2, 3, 4, 5]
string_list = convert_to_strings(integer_list)
print(f"Original List: {integer_list}")
print(f"Converted List: {string_list}")
