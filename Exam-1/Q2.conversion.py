# Conversion functions
def celsius_to_fahrenheit(celsius):
    return (celsius * 9/5) + 32
def celsius_to_kelvin(celsius):
    return celsius + 273.15
def fahrenheit_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5/9
def fahrenheit_to_kelvin(fahrenheit):
    return (fahrenheit - 32) * 5/9 + 273.15
def kelvin_to_celsius(kelvin):
    return kelvin - 273.15
def kelvin_to_fahrenheit(kelvin):
    return (kelvin - 273.15) * 9/5 + 32
def main():
    while True:
        print("\nTemperature Conversion Tool")
        print("1. Celsius to Fahrenheit")
        print("2. Celsius to Kelvin")
        print("3. Fahrenheit to Celsius")
        print("4. Fahrenheit to Kelvin")
        print("5. Kelvin to Celsius")
        print("6. Kelvin to Fahrenheit")
        print("7. Exit")   # Get user choice
        choice = input("Choose an option (1-7): ")
        if choice == "7":
            print("Thank you for using the Temperature Conversion Tool. Goodbye!")
            break # Get temperature input
        try:
            temp = float(input("Enter the temperature to convert: "))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue # Perform the chosen conversion
        if choice == "1":
            print(f"{temp}°C is {celsius_to_fahrenheit(temp):.2f}°F")
        elif choice == "2":
            print(f"{temp}°C is {celsius_to_kelvin(temp):.2f}K")
        elif choice == "3":
            print(f"{temp}°F is {fahrenheit_to_celsius(temp):.2f}°C")
        elif choice == "4":
            print(f"{temp}°F is {fahrenheit_to_kelvin(temp):.2f}K")
        elif choice == "5":
            print(f"{temp}K is {kelvin_to_celsius(temp):.2f}°C")
        elif choice == "6":
            print(f"{temp}K is {kelvin_to_fahrenheit(temp):.2f}°F")
        else:
            print("Invalid choice. Please select a valid option.") # Run the program
main()
