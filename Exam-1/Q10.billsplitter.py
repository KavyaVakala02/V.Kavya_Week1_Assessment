def get_input():
    bill_amt=float(input("enter the total bill:"))
    num_of_ppl=float(input("enter total number of people there:"))
    tip_percent=float(input("enter the tip percentage"))
    return(bill_amt,num_of_ppl,tip_percent)
def calculate_share(bill_amt,num_of_ppl,tip_percent):
    total= bill_amt+(bill_amt*tip_percent/100)
    per_person=total/num_of_ppl
    return per_person
    
def main():
    (bill_amt,num_of_ppl,tip_percent)= get_input()
    ans= calculate_share(bill_amt,num_of_ppl,tip_percent)
    print(f"share per each person is:{ans}")
main()
    