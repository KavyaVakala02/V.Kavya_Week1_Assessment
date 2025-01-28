def checkleap(year):
    if(year%4==0 and year%100 !=0) or (year % 4 == 0): return True
    else: return False
def get_input():
    year= int(input("enter the year:"))
    return year
def main():
    year=get_input()
    if checkleap(year): print(f"{year} is leap year")
    else: print(f"{year} is not a leap year")
main()