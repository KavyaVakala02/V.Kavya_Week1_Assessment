def factcalc(n):
    if n<0: return "error:cannot handle for negative numbers"
    res=1
    for i in range(1,n+1):
        res*=i
    return res
def main():
    try:                                           #try block to check and print the answer
        num=int(input("enter a number"))
        print(f"factorial of {num} is {factcalc(num)}")
    except:                                        #except block to handle the error
        print("error occoured")
main()
    