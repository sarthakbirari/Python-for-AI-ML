# Python Fundamentals 
# (Assignment 3)

# assignment problem




# Q1. Ask the user for a string and check whether it is a palindrome or not.
# A palindrome is a string which is same when  we read if forward and backward. Eg - "madam", "racecar" etc.

# [Hint: A palindrome string is equal to the reversed version of the string. we can use a loop to reverse the string manually.]


str = input("Enter the sentence:")

rev = ""

for ch in str:

    rev = ch + rev

    if (rev == str):
        print("It is palindrome")

    else:
        print("It is not palindrome")

#__________________________________________________________________________________________________________________________________________    

# Q2. Given a list of integers compute the average of all numbers in the list.


list = [10,30,25,15,5]

total = 0

for num in list:
    total = total + num

average = total / len(list)

print(average)


# _________________________________________________________________________________________________________________________________

# Q3. Input tw lists of integers from the user.Merge them into one list and sort the result.
# Eg: list1 = [1, 2, 7], list2 = [2, 4, 5]
#     result = [1, 2, 3, 54, 5, 7]


list1 = list(map(int, input("Enter first list: ").split()))

list2 = list(map(int, input("Enter second list: ").split()))

merged = list1 + list2

merged.sort()

print(merged)

# _________________________________________________________________________________________________________________________________________________

# Q4. Given a tuple of integers, create:

# - A tuple of all even numbers
# - A tuple of all odd numbers


tuple1 = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

list1 = []
list2 = []

for num in tuple1:

    if (num % 2 == 0):
      list1.append(num)
      
    else:
      list2.append(num)

even_tuple = tuple(list1)
odd_tuple = tuple(list2)

print(even_tuple)
print(odd_tuple)

#________________________________________________________________________________________________________________________

# Q5. Create a dictionary where:

# - Keys = student names
# - Values = marks(integer)

# Write a menu-based program where user presses a key ('A', 'B', 'C', 'D') depending on the operation they want to perform on the Dictionary:

# 1. 'A' - Add a student
# 2. 'B' - Update marks
# 3. 'C' - Search  for a student
# 4. 'D' - Display all students and marks


students = {}

choice = input("Enter the choice:")


if (choice == 'A'):

    name = input("Enter the student name:")
    marks = int(input("enter the number:"))
    
    students[name] = marks
    print("Student added")

elif (choice == 'B'):

    name = input("Enter the student name:")
    marks = int(input("enter the number:"))
    
    students[name] = marks

    print("Marks updated")

elif (choice == 'C'):

    name = input("Enter the name:")
    if name in students:
        print("Marks:",students[name])

    else:
        print("student not found")

elif (choice == 'D'):

    for name, marks in students.items():
        print(name, ":", marks)

else:
    print("Invalid choice")

# _______________________________________________________________________________________________________________________________________

# Q6. Given a list of words:

# words = ["apple", "banana", "kiwi", "cherry", "mango"]

# Create a dictionary that maps each word to its length.
# Example: {"apple": 5, "banana": 6, "kiwi": 4, ...}

words = ["apple", "banana", "kiwi", "cherry", "mango"]

dict1 = {}

for fruit in words:

    dict1[fruit] = len(fruit)

print(dict1)

# ________________________________________________________________________________________________________________________________________________________

# Q7. Write a program that takes a string from the user and prints the number of spaces in the string.

sentence = input("Enter the string:")

space = " "
count = 0
for word in sentence:
    if (space == sentence):
        count+=1

print(f"The space comes in the given {sentence} is {count}")
print(count)

# ________________________________________________________________________________________________________________________________________________________________

# Q8. Write a program to /
# check whether two lists share no common elements.
# [ Hint: use sets ]


List1 = [1,2,3,4]
List2 = [4,5,6,7]


set1 = set(List1)
set2 = set(List2)

common_element = set1.intersection(set2)

if (common_element == set()):
    print("No Common Elements")

else:
    print(f"common Elements:{common_element}")

# _____________________________________________________________________________________________________________________________

# Q9. Given a list, print all elements that appear more than once in the list.append


given_list = [1,2,1,3,4,2]

seen = set()
duplicate = set()

for num in given_list:
    if num in seen:
        duplicate.add(num)
 
    else:
        seen.add(num)

print("duplicate elements are:")
for i in duplicate:
    print(i)

# __________________________________________________________________________________________________________________________________________

# Q.10 Ask the user for a string and print:
# - All unique characters
# - The count of unique characters


word  = input("Enter the string:")

unique_ch = set(word)

print("The unique characters are:")
for i in unique_ch:
    print(i)

print(f"The count of unique characters is {len(unique_ch)}")


    


