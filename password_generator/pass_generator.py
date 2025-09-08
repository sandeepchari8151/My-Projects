import random as rd
import string as st

numbers = st.digits
special_char = ['@','#','$','%','&']
LC_letters = st.ascii_lowercase
UC_letters = st.ascii_uppercase
letters = st.ascii_letters

def pass_check(pas):
    if len(pas)<8:
        print("Password Must be atleast 8 characters..")
    has_upper = any(ch in UC_letters for ch in pas)
    has_number =any(ch in numbers for ch in pas)
    has_special  = any(ch in special_char for ch in pas)

    if not has_upper:
        print("upper case letter is missing..")
    if not has_number:
        print("number is missing")
    if not has_special:
        print("special character is missing")
    if has_number and has_special and has_upper:
        print("You password is strong..")
    else:
        return False
    

def pass_gen(pas):
    name=""
    name +=''.join(ch for ch in pas if ch in letters)
    name = name.capitalize()
    password =''.join(rd.choices(special_char))+''.join(rd.choices(numbers,k=4))
    newPass = name + password
    return newPass

def pas_strenth(pas):
    count=0
    if len(pas) <8:
        print("password must be atleast 8 characters")
        return
    has_upper = any(ch in UC_letters for ch in pas)
    has_number =sum(ch in numbers for ch in pas)
    has_special  = sum(ch in special_char for ch in pas)

    if has_number >2:
        count+=1
    if has_special >=1:
        count+=1
    if has_upper:
        count+=1
    
    if count ==3:
        print("Your password is Strong...")
    elif count ==2:
        print("Your password is medium...")
    else:
        print("Your password is Week...")

    

print("Hello welocome to password generator and validator..")
pas = input("Enter your password : ")
c = input("Do You want to check your password strength (y/n)").strip().lower()
if c == 'y':
    pas_strenth(pas)
c = input("Do You want to check what your missing (y/n)").strip().lower()
if c == 'y':
    pass_check(pas)
while True:
    choice = input("\nDo u want to make better password, press (y/n) or do you want to create your own, if yes press (s) ").strip().lower()
    if choice == 'y':
        print("Suggested Password: ",pass_gen(pas))
    elif choice =='s':
        new_pass =input("Enter new password..")
        pas = new_pass
        pass_check(new_pass)
    else:
        print("Thanks for using password generator..")
        break
    
    

    


