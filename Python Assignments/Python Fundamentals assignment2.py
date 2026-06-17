# PythonFundamentals(Assignment2)
# Assignment Problems




# Q1. Write a program that takes salary as input. Using Conditional statements, calculate ther final tax rate based on these rules:
# - if salary < 30000 -> 5%
# - if salary is  30000 - 70000 -> 15%
# - if salary > 70000 -> 25%



salary = int(input("Enter the salary"))

if (salary < 30000):
    print("tas rate 5%")

elif (salary >= 30000 and salary < 70000):
    print("tax rate 15%")

else:
    print("tax rate 25%")

# ________________________________________________________________________________________________________________________________________________

# Q2. Write a function that takes two integers a and b and prints all even numbers between them (inclusive).

def even_num(a,b):

    for i in range(a, b+1):
        if ( i%2==0 ):
            print(i)
        

print(even_num(2,15))

# _____________________________________________________________________________________________________________________________________________________

# Q3. Write a function that prints the digits of a number, n.
# for eg: n = 312, there are 3 digits in it 3, 1, 2 and we need to print them.
    

def print_digi(n):

    while (n > 0):

        digit = n % 10
        print(digit)
        n = n // 10


print(print_digi(312))

# _______________________________________________________________________________________________________________________________________

# Q4. Write a function to return the count the number of digits ina number, n.


def count_digi(n):

    count = 0
    while (n > 0):
        n = n // 10
        count+=1

    return count
    
print(count_digi(312))

# ____________________________________________________________________________________________________________________________

# Q5. Write a function to return the sum of digits of a number, n.

def sum_digi(n):

    sum = 0
    while (n > 0):
        
        digit = n % 10 
        sum+=digit

        n = n // 10

    return sum

print(sum_digi(1234))

# _______________________________________________________________________________________________________________________________________________

# Q6. Write a program to print all numbers from 1 to 100 that are divisible by both 3 and 5.


for i in range(1,101):
    if ( i%3==0 and i%5==0 ):
        print(i)

# ___________________________________________________________________________________________________________________________________________________________

# Q7. Design a program to continuously input a number n from user and print if it is positive or negative until the user enters "Quit".



while True:
    n = input("Enter the number:")

    if (n == "quit"):
        break
    n = int(n)

    if (n > 0):
        print("Positive")

    elif(n < 0):
        print("Negative")

    else:
        print("Number neither positive nor negative")

# _________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Q8. Lets create a Simple Calculator that performs arithmetic operations. Create a function calculator(a, b, operation) that pewrforms addition, substraction, multiplication, or division based on the operation parameter.
# ['operation' parameter can have values '+', '-', '*' and '/']



def calculator(a, b, operation):

    if (operation == '+'):
        return a + b
    
    elif (operation == '-'):
        return a - b

    elif (operation == '*'):
        return a * b

    elif (operation == "/"):
        return a / b

print(calculator(2,2,'='))    


# ________________________________________________________________________________________________________________________________________________________

# Q9. Write a function is_prime(n) that returns True if n is prime number and False otherwise, using a loop.else
# [hint: 

    #    1. We only check prime for 2 or number greater than 2. 2 is the smallest prime number.
    #    2. A non-prime number, n, will get divided by atleast one number in range[2, n-1].
    #    eg - For number 9 we will check in range(2,8) and it will  get divided by 3. So 9 is non-prime and we will return false for it.
    #         For number 7 we will check in range (2, 6) and it won't get divided by any.So 7 is prime and we will return true for it.]


def is_prime(n):

     for num  in range(2, n-1):
        if (n % num == 0):
            return False
    
     else:
        return True 


print(is_prime(12))

# ______________________________________________________________________________________________________________________________________________________________________________

# Q10. Let's create a "Numbner Guessing Game". given a secret number (already decided by you), write a program that asks the user to guess it and prints:

# - "Too high" if the guess is above the number
# - "Too low" if the guess is below 
# - "Correct" if the guess matches

while True:
    number = int(input("guess the number:"))

    if (number == 2):
        print("Correct")
        break

    elif (number < 2):
        print("Too low")

    else:
        print("Too high")

        


