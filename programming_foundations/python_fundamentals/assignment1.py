'''
#1.WAP THAT TASK THE USER FOR THIER NAME , AGE PRINT A SENTENCE LIKE : Hello Deep, you are 21 years old!
name = input("enter your name:")
age = input("enter your age:")

print("Hello", name, ",you are", age, "years old !")
'''

'''
#2.Take two numbers as input from the user and print their sum, difference, product, and quotient.
a = float (input("enter number a:"))
b = float (input("enter number b:"))

sum = a + b
diff = a - b
product = a * b
quotient = a / b

print("sum of a & b:",sum)
print("difference of a & b:",diff)
print("product  of a & b:",product)
print("quotient of a & b:",quotient)
'''

'''
#3.Ask the user to enter two integers and one float. Convert them all to floats and print their average

a = int (input("enter number a:"))
b = int (input("enter number b:"))
c = float (input("enter number c:"))

avg = float((a + b + c)/3)
print("average of a , b , c :",avg)
'''

'''
#4.The user enters a string containing a number (e.g., ). Convert it to:
• an integer
• a float
• a string again
Print all three values with their types.

num =  input("enter a num:")

num_int = int(num)
num_float = float(num)
num_str = str(num)

print("Integer:",num_int, "Type:",type(num_int))
print("Float:",num_float, "Type:",type(num_float))
print("String:",num_str, "Type:",type(num_str))
'''

'''
#5.Evaluate and print the result of the following expression:x = 10 + 3 * 2 ** 2
Based on what you learnt in the lecture explain why the output is what it is.

x = 10 + 3 * 2 ** 2
print(x)
'''

'''
#6.Write a program to swap values of two numbers entered by the user.
a = input("enter number a:")
b = input("enter number b:")

temp = a
a = b
b = temp

print("After swapping:")
print("a =", a)
print("b =", b)
'''
'''
#7.Ask the user for a temperature in Celsius (string input). Convert it to , 
then calculate and print temperature in Fahrenheit.
Conversion formula: FahrenheitTemp = (CelsiusTemp ∗ (9/5)) + 32

Celsius_temp = input("temperature in celsius:")
Celsius_temp = float(Celsius_temp)
Fahrenheit_temp = ((Celsius_temp * (9/5)) + 32)
print ("temperature in fahrenheit:",Fahrenheit_temp)
'''

'''
#8.Take the radius (r) as user input and print the area.
Use the formula: Area = π * r2
(value of π = 3.14)

rad = input("enter radius of circle:")
rad = float(rad)
pi = 3.14
area = float( pi * rad * rad)
print("area of circle is:",area)
'''

'''
#9.Ask the user for: Principal (P), Rate (R), Time (T). Convert all to and 
compute simple interest:
SI = (P ∗ R ∗ T)/100

p = float (input ("enter principal:"))
r = float (input("enter rate:"))
t_years = float (input("enter time(in years):"))

t_months = t_years * 12

si = ((p*r*t_months)/100)
print("simple intrest:",si)
'''

'''
#10.Take a decimal number as input (like 45.18 ) and output its:
• integer part -45
• fractional part -.18
'''
num = float(input("enter decimal number:"))

integer_part = int(num)
fraction_part = num - integer_part

print("Integer part:",integer_part)
print("Fraction part:",fraction_part)