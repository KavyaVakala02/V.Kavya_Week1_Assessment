def buzz(n):
    for i in range(1,n+1):   #running loop till n 
        if i%3==0: print("Fizz")         #numbers divisible by 3
        elif i%5==0: print("Buzz")       #numbers divisible by 5
        elif i%3==0 and i%5==0: print("FizzBuzz")   #numbers divisible by 3 and 5
        else: print(i)          #other numbers
def main():
    buzz(100)    #function call
main()
    