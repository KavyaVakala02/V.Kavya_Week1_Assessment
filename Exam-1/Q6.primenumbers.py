def is_prime(number):
    if number < 2:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True
def start_end_range(start,end):
    for num in range(start,end+1):
        if(is_prime(num)):
            print(num)
def main():
    start=int(input("enter start range:"))
    end= int(input("enter end range"))
    print(f"Prime Numbers between {start} and {end} are")
    start_end_range(start,end)
main()
    
