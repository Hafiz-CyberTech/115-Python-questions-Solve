# Function to convert Celsius to Fahrenheit
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32

# Main program
if __name__ == "__main__":
    # Ask the user for input
    celsius = float(input("Enter temperature in Celsius: "))
    
    # Convert the Celsius temperature to Fahrenheit
    fahrenheit = celsius_to_fahrenheit(celsius)
    
    # Print the result
    print(f"{celsius} degrees Celsius is equal to {fahrenheit} degrees Fahrenheit.")