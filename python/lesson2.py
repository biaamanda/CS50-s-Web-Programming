name = input("Name: ")
# print("Hello, " + name + "!")
print(f"Hello, {name}!")



n = int(input("Number: "))
if n > 0:
    print("Number is Positive")
elif n < 0:
    print("Number is Negative")
else:
    print("Number is equals to zero")
    
    

name = "John"
print(name[0])  # J

list = ["apple", "banana", "cherry"]
print(list[0])  # apple


#set - unordered collection of unique items

#sort - modify the order of the list
#append
#add
#remove
#len - length of the list

#loops
# can also be done with lists or even add values to each element of the list. eg: foodType = {"apple": "fruit", "carrot": "vegetable"} print(foodType["apple"]) #fruit
for i in range(6):
    print(i)
    
#functions
def square(x):
    return x * x
for i in range(10):
    print(f"The square of {i} is {square(i)}")
    
#classes
class Point():
    def __init__(self, input1, input2):
        self.x = input1
        self.y = input2
        
p = Point(2, 3)
print(p.x)  # 2
print(p.y)  # 3

class Flight():
    def __init__(self, capacity):
        self.capacity = capacity
        self.passengers = []
        
    def add_passenger(self, name):
        if not self.passengers.append(name): # adds someone new to the list of passengers
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity - len(self.passengers) # returns the number of open seats 
        
flight = Flight(3)

people = ["Alice", "Bob", "Charlie", "David"]
for person in people:
    if flight.add_passenger(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}.")

#decorators
def announce(f):
    def wrapper():
        print("About to run the function...")
        f()
        print("Finished running the function.")
    return wrapper

@announce
def hello():
    print("Hello, world!")
    
#lambda
people = [
    {"name": "Alice", "age": 30},
    {"name": "Bob", "age": 25},
    {"name": "Charlie", "age": 35}
]

people.sort(key=lambda person: person["name"])
print(people)

#exceptions
import sys
try: 
    x = int(input("x: "))
    y = int(input("y: "))
except ValueError:
    print("Error: Invalid input.")

try:
    result = x / y
except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

print(f"{x} / {y} = {result}")