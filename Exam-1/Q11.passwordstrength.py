def get_input():
    password= input("enter the password")
    return password
def check_password_strength(password):
    if len(password)<8: print("password is too weak. enter more than 8 characters")
    upper= any(char.isupper() for char in password)
    lower=any(char.islower() for char in password)
    digits= any(char.isdigit() for char in password)
    specialchar= any(char in "?/\$%#@!&*" for char in password)
    if not upper: return("weak.enter atleast one upper case")
    if not lower: return ("weak. enter atleast one lower case")
    if not digits: return("weak. enter atleast one numerical digits")
    if not specialchar: return("weak. enter atleast 1 special characters")
    return("password is strong")
def main():
    password= get_input()
    ans=check_password_strength(password)
    print (ans)
main()