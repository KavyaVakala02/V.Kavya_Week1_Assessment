def bankloan(salary,age,credit):          #function to check the eligibility of the loan 
    if(age<18): print("rejected. Too young to get the loan")
    elif salary<10000: print("rejected.Salary is low to get the loan")
    elif credit<500: print("rejected. Credit score is low to get loan")
    else: print("bankloan approved")
def get_input():                            #function to get input from user 
    salary=int(input("enter salary"))
    age=int(input("enter age "))
    credit=int(input("enter credit score "))
    return(salary,age,credit)
def main():
    (salary,age,credit)=get_input()
    bankloan(salary,age,credit)
main()