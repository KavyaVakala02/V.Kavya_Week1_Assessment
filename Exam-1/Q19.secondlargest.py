def find_second_largest(numbers):
    largest = second_largest = float('-inf')  # Smallest value is initialised to largest and second largest variable
    for num in numbers:
        if num > largest:  # Update largest and second largest
            second_largest, largest = largest, num
        elif num > second_largest and num != largest:  # Update only second largest
            second_largest = num
    return second_largest if second_largest != float('-inf') else "No"
def main():
    nums=list(map(int,input("enter numbers separated by spaces").split())) #input from user
    print("second largest",find_second_largest(nums))
main()