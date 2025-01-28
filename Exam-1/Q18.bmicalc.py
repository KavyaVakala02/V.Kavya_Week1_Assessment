def get_input():                 #taking input from user                                       
    weight= float(input("enter weight in kg:"))
    height= float(input("enter height in meters"))
    return (weight,height)
def calcbmi(weight,height):       #calculating bmi
    bmi= (weight)/(height**2)
    if(bmi<18): print("underweight")             # predicting underweight
    elif (bmi<25): print("normal")                #predicting normal
    elif (bmi<35): print("overweight")            
    else: print("obese")                          #if weight is more,then obesity
    return bmi
def main():
    (weight,height)= get_input()                    #calling input function and assigning to 2 variables
    print("BMI is:",calcbmi(height,weight))           #printing result by calling calcbmi function
main()