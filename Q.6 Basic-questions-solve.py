# Question:  Write a Python function that takes a variable as input and returns the data type of the variable as a string (e.g., “int”, “float”, “str”, “list”, etc.).


#Function for Data Type Checker:

#------------------------------------
def get_data_type(variable):
    return type(variable).__name__
    
    
# Examples
print(get_data_type(50))          # Output: int
print(get_data_type(3.14))        # Output: float
print(get_data_type("Hafiz"))     # Output: str
print(get_data_type([2, 3, 4]))   # Output: list
print(get_data_type((1, 2, 3)))   # Output: tuple
print(get_data_type({'a': 1}))    # Output: dict
print(get_data_type({1, 2, 3}))   # Output: set