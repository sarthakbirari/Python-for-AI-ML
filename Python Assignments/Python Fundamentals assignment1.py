# Python Fundamentals 
# ( Assignment problems 1 )



# Q1. Write a program that asks user for their name and age,then prints a sentence like:
    # ( Hello Sarthak, you are 21 years old )


name = input("Enter the name:")
age = int(input("Enter the age"))

print("Hello", name, ",", "you are", age, "years old")

# _______________________________________________________________________________________________________________________________

# Q2. Take two numbers as input from the user and print their sum, difference, product, and quotient.


num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))

sum = (num1 + num2)
difference = (num1 - num2)
product = (num1 * num2)
quotient = (num1 / num2)

# _______________________________________________________________________________________________________________________________________________________

# Q3. Ask the user to enter two integers and one float. Convert them all to floats and print their average.


num1 = int(input("Enter the number:"))
num2 = int(input("Enter the number:"))
num3 = float(input("Enter the number:"))

avg = float((num1+num2+num3)/3)

print("The average is:", avg)



digit = input("Enter the digit")

print(int(digit))
print(float(digit))
print(digit)

print(type(int(digit)))
print(type(float(digit)))
print(type(digit))


# ___________________________________________________________________________________________________________________

# Q5. Evalute and print the result of the following expression:

# x = 10 + 3 * 2 ** 2

x = 10 + 3 * 2 ** 2
print(x)

# _________________________________________________________________________________________________________________________

# Q6. Write a program to swap values of two numbers entered by the user.



a = int(input("Enter the number"))
b = int(input("Enter the number"))

a,b = b,a

print(a.b)

# ________________________________________________________________________________________________________________________________________

# Q7. Ask the user for a temperature in celcius(string input). Convert it to float, then calculate and print temperature in Fahrenheit.

# FahrenheitTemp=(CelsiusTemp∗(9/5))+32


temperature = input("Enter the temperature in celsius:")

CelsiusTemp = float(temperature)

FahrenheitTemp = (CelsiusTemp*(9/5))+32

print(FahrenheitTemp)

# _________________________________________________________________________________________________________________________________________________________________

# Q8. Take the radius (r) as user input and print the area.\
# Use the formula: Area = 3.14*r**2


r = int(input("Enter the radius:"))

Area = 3.14*r**2

print(Area)

# ______________________________________________________________________________________________________________________________________________

# Q9. Ask the user: Principle(P), Rate(R), Time(T). Convert all to float and compute simple interest.InterruptedError
# SI = (P*R*T)/100


p = int(input("Enter the Principle:"))
r = int(input("Enter the Rate:"))
t = int(input("Enter the Time:"))

P = float(p)
R = float(r)
T = float(t)


SI = (P*R*T)/100
print(SI)

# ________________________________________________________________________________________________________________________________________

# Q10. Take a decimal number as input(like 45.7) and outout its:

# - integer part: 45
# - fractional part: 7


dec_num = float(input("Enter the decimal number:"))

int_part = int(dec_num)
frac_part = (dec_num - int_part)

print(int_part)
print(frac_part)

