# Python Fundamentals: Assignment Problems
# (Assignment5)


# Q1. Create a program that:

# 1. Opeans a file "names.txt" in the write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then opens the same file in read mode and prints all names

with open("names.txt", "w") as f:
    
    for name in range(5):
        name = input("Enter the name:")
        f.write(name + "\n")
       

with open("names.txt", "r") as f:
    data = f.read()
    print(data)



# ___________________________________________________________________________________


# Q2. Create a program that:

# 1. Opens a file "log.txt" in append mode 
# 2. Adds a new log entry (like "Program run successfully")
# 3. Opens the file in read mode and prints all logs


with open("log.txt", "a") as f:

    f.write("Program run successfully \n") 
    

with open("log.txt", "r") as f:

    print(f.read())


# ___________________________________________________________________________________________________________


# Q3. Create a program that:

# 1. Has a list of numbers: [5, 10, 15, 20, 25]
# 2. Uses a list comprehensions to create a new list with only numbers greater than 15
# 3. Print the new list

list1 = [5, 10, 15, 20, 25]

list2 = [num for num in list1 if num > 15]
print(list2)


# _________________________________________________________________________________________________________________________



# Q4. Create a Python dictionary of 3 cites and their populations. Save it to "data.json". 

# 1. Then load the JSON and print each city and its populations.
# 2. Ask the user for a new city & its population - update this info in the json file.

import json 

dict1 = {
    "Bhopal": 50_000,
    "Indore": 80_000,
    "Jaipur": 10_0000
}


with open("data.json", "w") as f:

    json.dump(dict1, f, indent = 4)

with open("data.json", "r") as f:
    data = json.load(f)
    for city, population in data.items():
        print(city, population)

city = input("Enter the city:")
population = int(input("Enter the population:"))

data[city] = population


with open("data.json", "w") as f:

    json.dump(data, f, indent = 4)


# _________________________________________________________________________________________________________


# Q5. Write a program that tries to open "data.txt" in read mode. IF the file does not exist, catch the exception and print "File not found!".


try:
    with open("data.txt", "r") as f:
        data = f.read()

except FileNotFoundError:
    print("File  not found!")

else:
    print(data)

finally:
    print("Program ended")









