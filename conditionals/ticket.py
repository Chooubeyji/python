#movie tickets are priced based on age : $12 for adults (18 and over),$8 for children . Everyone gets a $2 discount on wednesday
age = int(input("Enter the age : "))
day = input("Enter the day : ")

price = 12 if age >= 18 else 8

if day == "wednesday" :
    price = price-2
print(" ticket price for you is: $ " ,price)