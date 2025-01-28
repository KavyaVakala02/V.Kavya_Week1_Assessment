def separateodd(num):   #separating odd number
    odds=[]               #empty list to store odd numbers
    for i in num:           
        if(i%2!=0):           #checking if number is odd
            odds.append(i)   #appending to the list if the number is odd
    return odds
def separateeven(num):          #function to separate even numbers
    evens=[]                     #creating empty list to store even numbers
    for i in num:                  
        if i%2==0 :                  #checking if the number is even 
            evens.append(i)           #appending all even numbers to empty list
    return evens
def get_input():
    num=list(map(int,input("enter the list of numbers:").split()))  #function to get list of numbers from the user
    return num
def main(): 
    num=get_input()                  #calling the functions
    odds=separateodd(num)         
    evens=separateeven(num)
    print("odd numbers",odds)
    print("even numbers",evens)
main()
        