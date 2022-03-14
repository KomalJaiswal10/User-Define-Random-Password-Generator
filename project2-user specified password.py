import string
import random

num = input("Enter the number of characters you want in ur password :")


spunct = '@$&%_#.'
s_all = string.ascii_letters + spunct + string.digits 


password = ""

if num.isdigit():
    while len(password) != (int(num)):
        password += (random.choice(s_all))
    print("Your Password : ", password)

else:
    print("Invalid I/P")
    





