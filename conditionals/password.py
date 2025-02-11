#check the password is strong or not
password = input("Enter the password :")
password_length = len(password)
print("length of password is" ,password_length)
if password_length >= 6 :
    print("password is strong")
elif password_length >=3 :
    print("password is average")
else:
    print("weak password")        
