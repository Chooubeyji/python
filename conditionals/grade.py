#assign a letter grade based on a student score : A (90-100), B(80-89), C(70-79), D(60-69), F(below 60) 
name = input("enter your name :") 
marks = int(input("Enter your marks :"))
if marks >=101:
    print("please enter valid marks ")
    exit()
if marks >= 90 :
    print("Grade of" ,name ,"is A")
elif marks >= 80 :
    print("Grade of" ,name ,"is B")    
elif marks >= 70 :
    print("Grade of" ,name ,"is C")    
elif marks >= 60 :
    print("Grade of" ,name ,"is D")  
else :
    print(name , "is fail!!")      
