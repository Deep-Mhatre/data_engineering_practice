'''
Conditional Statements
keyworf: if, elif, else
'''
'''
#1.if
age = int(input("enter your age:"))

if age >= 18:
    print("you can vote")

if age <= 18:
    print("you cant vote")
'''
'''
#2.else
age = int(input("enter your age:"))

if age >= 18:
    print("you can vote")

else:
    print("you can't vote")
'''
'''
#3.elif
color = input("enter traffic color:")

if color == "red":
    print("stop")
elif color == "green":
    print("go")
elif color == "yellow":
    print("stay")
else:
    print("wrong color for traffic light")
'''
'''
#examples 1. WAP to describe <13= child, 13-18=teenager,18+=adult
age = int(input("Enter age:"))

if age < 13:
    print("you are a child")
elif (age >= 13 and age <18):
    print("you are teenager")
else:
    print("you are an adult")
'''
'''
#2.WAP to if username="admin", password="pass" you can login
username = str(input("Enter Username:"))
password = str(input("Enter Password:"))

if (username == "admin" and password == "pass"):
    print("Login Sucessfully")
elif (username == "admin" and password != "pass"):
    print("You entered incorrect password")
elif (username != "admin" and password == "pass"):
    print("You entered incorrect username")
else:
    print("incorrect username and password")
'''
'''
#3. WAP to check if it is multiple of 5

num = int(input("Enter num:"))

if num % 5 == 0:
    print(num,"is multiple of 5")
else:
    print("not multiple of 5")
'''

#4. WAP to print if any num is odd or even

num = int(input("Enter num:"))

if num % 2 == 0:
    print(num,"is even number")
else:
    print(num,"is odd number")