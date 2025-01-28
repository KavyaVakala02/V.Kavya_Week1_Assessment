def generatePattern(n, rev):
    if n==1: print("*")
    if rev:
        for i in range(n,0,-1):
            print ("*"*i)
    else:
        for i in range(1,n+1):
            print("*"*i)
def get_input():
    n= int(input("enter number of rows"))
    return n
def main():
    n=get_input()
    rev=input("do you want to print in rev?").lower()
    if rev=="yes":
        generatePattern(n,rev=True)
    else:
        generatePattern(n,rev=False)
main()
        
    
    