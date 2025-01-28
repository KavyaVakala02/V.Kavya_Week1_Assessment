def check_palindrome(val):               #function to check palindrome
    val=str(val).replace(" ","").lower()  #converting input into string, taking all the empty spaces off and converting it to lower characters
    val==val[::-1]                          #reversing the string and checking if it is same
    return val                              #returning the value
def main():                               
    while True:
        val= input("enter string:")
        if check_palindrome(val): print("it is a palindrome")
        else: print("it is not a palindrome")
main()