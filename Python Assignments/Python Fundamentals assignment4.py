# Python Fundamentals:
# (Assignment4)

# Concept: Classes & Objects

# Q1. Create a BankAccount class with attributes account_number, owner_name, and balance. Add methods to deposit, withdraw, and check balance.



class BankAccount:

    def __init__(self,account_number, owner_name, balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        
    def withdraw(self, withdraw_amount):

        if (withdraw_amount > self.balance):
            print("Insufficient Balance!")

        else:
            print(withdraw_amount)

    def check_balance(self):

        return self.balance
    

p1 = BankAccount(1234, "Sarthak", 50_000)
print(p1.owner_name, p1.account_number, p1.balance)

p1.deposit(5000)
p1.withdraw(2000)
p1.check_balance()

# _____________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Classes & Objects

# Q2. Create a class Book with the following attributes:
# - title 
# - author
# - list of reviews

#  And add methods to:
# - add a new review
# - count reviews 
# - display all reviews 


class Book:

    def __init__(self, title, author, reviews = [] ):

        self.title = title
        self.author = author
        self.reviews = reviews
        
#    add a new review
    def add_new_review(self):
        self.reviews.append()

#    count reviews 
    def count_reviews(self):
        print(f"There are {len(self.reviews)}")

#    display all reviews
    def display_reviews(self):
        print(self.reviews)


book1 = Book("Build Don't Talk", "Raj Shamani", ["good", "excellent", "outstanding"])
book2 = Book("Rich dad Poor dad", "Robert", ["good", "mind blowing"])

print(book1.title, book1.author)
print(book2.title, book2.author)

book1.add_new_review("Nice")
book1.count_reviews()
book1.display_reviews()

book2.add_new_review("Amazing")
book2.count_reviews()
book2.display_reviews()

# ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Encapsulation

# Q3. Create a class Student with private attributes _name, roll_no, and _marks. Provide getter and setter methods with validation (e.g., marks cannot be negative, roll number has to be between 1 & 100 & name cannot be empty).



class Student:

    def __init__(self, name, roll_no, marks):

        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

#     setter function for name
    def set_name(self):
        if (self.__name == ()):
            print("Error")

        else:
            print(f"Name: {self.__name}")

#    setter  function for roll number
    def set_roll_no(self):
        if (self.__roll_no > 1 and self.__roll_no < 100):
            print(f"Roll Number: {self.__roll__no}")

        else:
            print("Roll Number is not found")

#    setter function fo marks
    def set_marks(self):
        if (self.__marks <= 0):
            print("Invaild marks")

        else:
            print(f"Marks: {self.__marks}")
        

#   getter function for name
    def get_name(self):
        return self.__name

#   getter function for roll number
    def get_roll_no(self):
        return self.__roll_no

#   getter function for marks
    def get_marks(self):
        return self.__marks

s1 = Student("Sarthak", 21, 95)
s2 = Student("Ritika", 22, 80)

s1.set_name()
s1.set_roll_no()
s1.set_marks()

s1.get_name()
s1.get_roll_no()
s1.get_marks()

s2.set_name()
s2.set_roll_no()
s2.set_marks()

s2.get_name()
s2.get_roll_no()
s2.get_marks()

# _________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Function Overriding

# Q4. Create a class Shape with a method area().
#     Create subclass Circle, Rectangle, and Triangle that override the area() method.


class Shape:

    def area(self):
        pass
        

class Circle(Shape):

    def area(self, radius):
        self.radius = 3.14 * radius ** 2
            

class Rectangle(Shape):

    def area(self, length, breadth):
        self.length = length
        self.breadth = breadth
        return length * breadth

        
class Triangle(Shape):

    def area(self, base, height):
        self.base = base
        self.height = height
        return (1/2) * base * height

circle = Circle()
circle.area(24) 

rectangle = Rectangle()
rectangle.area(50, 20)

triangle = Triangle()
triangle.area(10,20)

# ____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Inheritance

# Q5. Create a base class Vehicle with attributes like brand and model.
#     Create two subclass Car and Bike that add extra attributes - seats (in Car) & engine_cc (in Bike) .

class Vehicle:

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 

class Car(Vehicle):  #multilevel inheritance used

    def __init__(self, seats):
        self.seats = seats 


class Bike(Vehicle):

    def __init__(self, engine_cc):
        self.engine_cc = engine_cc


car1 = Car("BMW", "M5", 4)
car2 = Car("Mercedes", "S class", 4)

print(car1.brand, car1.model, car1.seats)
print(car2.brand, car2.model, car2.seats)


bike1 = Bike("Kawasaki", "ZX10R", "1000cc")
bike2 = Bike("Kawasaki", "Z900", "900cc")

print(bike1.brand, bike1.model, bike1.engine_cc)
print(bike2.brand, bike2.model, bike2.engine_cc)


# _____________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Abstraction

# Q6. Create an abstract class Employee with an abstract method calculate_salary().
#     Create subclasses Intern, FullTimeEmployee, and ContractEmployee that implement the method differently.


from abc import ABC, abstractmethod 

class Employee:

    @abstractmethod
    def calculate_salary(self):
        pass


class Intern(Employee):

    def calculate_salary(self, intern_salary):
        self.intern_salary = intern_salary
        print(f"The salary of the Intern is {self.intern_salary}")


class FullTimeEmployee(Employee):

    def calculate_salary(self, fulltime_employee_salary, bonus_salary):
        self.fulltime_employee_salary = fulltime_employee_salary
        self.bonus_salary = bonus_salary
        print(f"The salary of the full time employee is {self.fulltime_employee_salary + self.bonus_salary}")


class ContractEmployee(Employee):

    def calculate_salary(self, perhour_rate, time):
        self.perhour_rate = perhour_rate
        self.time = time
        print(f"The salary of the Contract Employee is {self.perhour_rate * self.time}")


e1 = Intern()
e1.calculate_salary(20_000)

e2 = FullTimeEmployee()
e2.calculate_salary(50_000, 5000)

e3 = ContractEmployee()
e3.calculate_salary(500,4)

# ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Constructor Overloading (with Default parameters)

# Q7. Create  a class Person that allows the constructor to work with:
#    - name only
#    - name + age
#    _ name + age +address

# As direct constructor overloading (multiple constructors) are not allowed but we have to use default parameters to simulate constructor overloading.


class Person:

    name = "Krishna"
    age = 20 
    address = "arera colony, Bhopal"

    def __init__(self):

        print(f"The name is {self.name}")

    def __init__(self):

        print(f"The name is {self.name} and age is {self.age}")

    def __init__ (self):

        print(f"The name is {self.name}, age is {self.age}, the address is {self.address}")


p1 = Person()


# __________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# Concept: Instance & Class Attributes 

# Q8. Create a class Player with:
#     - a class variable player_count
#     - instance variables name and level

# Track how many players were created.


class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count+=1


p1 = Player("Sarthak", 70)
p2 = Player("Ritika", 50)
p3 = Player("Krishna", 80)
p4 = Player("Virat", 65)
p5 = Player("Rohit", 75)

print(p1.name, p1.level)
print(p2.name, p2.level)
print(p3.name, p3.level)
print(p4.name, p4.level)
print(p5.name, p5.level)

print(Player.player_count)


# ___________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________

# Concept: Multiple Inheritance

# Q9. Create the following classes: Herbivore, Carnivore, Omnivore with some attributes & methods. Then create a class Bear that inherits from all the above classes to showcase how multiple inheritance works. 


class Herbivore:

    def __init__(self, name, diet):

        self.name = name
        self.diet = diet


    def eat_plant(self):
        print("Eat plants")


class Carnivore:

    def __init__(self, sound):

        self.sound = sound

    def eat_meat(self):
        print("Eat meat")


class Omnivore:

    def eat_both(self):
        print("Eat both")


class Bear(Herbivore, Carnivore, Omnivore):

    def behaviour(self):
        print("Mostly dangerous")

bear = Bear("Bear", "Eat both plants and meat", "Ghraaa...")

print(bear.name, bear.diet, bear.sound)


# __________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# Concept: OOP

# Q10. Mini Project - OOP Chat System
 
# Let's create a Chat System using OOPs concepts. We have to create classes:
# - User
# - Message
# - ChatRoom

#  And we have to implement functions:
# - sending messages
# - veiwing chat history
# - user joining and leaving the chatroom.


        

    
class User:

    def __init__(self, username):
        self.username = username

    def __str__(self):
        return self.username


class Message:

    message_counter = 1

    def __init__(self, sender, content):

        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter+=1

    def __str__(self):

        return f"({self.id}) {self.sender.username}: {self.content}" 



class ChatRoom:

    def __init__(self):

        self.users =[]
        self.messages =[]

    def join(self, user):

        if user not in self.users:

            self.users.append(user)
            print(f"{user.username} joined the chatroom")

        else:
            print(f"{user.username} is already in the chatroom")


    def broadcast(self, sender, content):

        if sender in self.users:

            message = Message(sender, content)

            self.messages.append(message)

            print(message)

        else:
            print("You cannot send message because you have not joined the chatroom.")


    def leave(self, user):

        if user in self.users:

            self.users.remove(user)
            print(f"{user.username} left the Chatroom")

        else:
            print("User not found")


    def show_chat_history(self):

        print("Chat History:")
        for msg in self.messages:
            print(msg)

    
    def show_total_users(self):

        print(len(self.users))


    def show_active_users(self):

        for user in self.users:
            print(f"Active member:{user}")




room = ChatRoom()

u1 = User("Sarthak")
u2 = User("Ritika")
u3 = User("Krishna")

room.join(u1)
room.join(u2)

room.broadcast(u1, "Hello")
room.broadcast(u2, "Hii")

room.join(u3)

room.broadcast(u3, "Hey, What's up guys")

room.show_total_users()

room.show_chat_history()

room.leave(u1)

print(room.users)

room.show_active_users()










    









