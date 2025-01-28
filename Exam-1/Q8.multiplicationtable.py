# Function to generate the multiplication table
def generate_multiplication_table(number, start, end):
    print(f"Multiplication Table for {number}:")
    for i in range(start, end + 1):
        print(f"{number} x {i} = {number * i}")
# Main function to get input and generate the table
def main():
    # Get the number and range from the user
    number = int(input("Enter the number for the multiplication table: "))
    start_range = int(input("Enter the starting range: "))
    end_range = int(input("Enter the ending range: "))
    # Generate and display the table
    generate_multiplication_table(number, start_range, end_range)
# Run the program
main()
