# num2 = 2 + 3j
# num = complex(2, 3) #  (i real, j complex)

# print(num.real, num.imag)

# abs(-5.5) #absoulte value 
# round(5.5) # = 6
# round(5.49, 1) # = 5.5

# #Enums
# from enum import Enum

# class State(Enum): 
#     INACTIVE = 0
#     ACTIVE = 1

# print(State.ACTIVE.value)
# print(State['ACTIVE'])
# print(State(1))
# print(list(State))
# print(len(State))

# # User input 

# age = input("What is your age? ")
# print("Your age is " + age)

### Python Data Structures, Lists, Tuples, Dictionaries, Sets
# # Lists

# dogs = ["Roger", "Syd", 1, True, "Quincy", 7]
# print("Roger" in dogs)
# print(dogs[2])
# dogs[2]="Boe"
# print(dogs)
# print(dogs[-1])
# print(dogs[2:4])
# print(dogs[2:])
# print(dogs[:3])
# dogs.append("Judah")
# print(dogs)
# dogs.extend(["aika", 5])
# print(dogs)
# dogs += ["Aika", 5] # same as extend
# print(dogs)
# dogs.remove("Quincy")
# print(dogs)
# print(dogs.pop())
# print(dogs)
# dogs.insert(2, "Test")
# print(dogs)
# dogs[1:1] = ["Test1", "Test2"]
# print(dogs)
# dogscopy = dogs[:] #copy the list 
# dogscopy.remove(5)
# dogscopy.remove(7)
# dogscopy.remove(True)
# dogscopy.sort(key = str.lower) # only same time, not mixed & key = str.lower will sort uppercase or lowercase together 
# print(dogscopy)
# print(dogs)
# # sorted(dogs, key=str.lower) # sorting without modifying original list

# # Tuples

# names = ("Roger", "Syd", "Boe")
# print(names[0])
# print(names.index("Roger"))
# print(names[-1])
# print(len(names))
# print("Roger" in names)
# print(sorted(names)) 
# newTuple = names  + ("Tina", "Quincy")
# print(newTuple)
# print(names)

# # Dictionaries
# dog = { "name": "Roger", "age": 8, "color": "green" }
# dog["name"] = "Syd"
# print(dog["name"])
# print(dog.get("color", "brown")) #set default value to "brown" if there's no color key 
# print(dog.pop("name"))
# print(dog)
# print(dog.popitem())
# print("color" in dog)
# print(list(dog.keys()))
# print(list(dog.values()))
# print(list(dog.items()))
# dog["favorite food"] = "Meat"
# del dog["age"]
# print(dog)
# print(len(dog))
# dogcopy = dog.copy() #copy a dict

# # Sets

# set1 = {"Roger", "Syd", "Aika"}
# set2 = {"Roger"}
# set3 = {"Luna"}
# intersect = set1 & set2
# print(intersect)
# union = set1 | set3
# print(union)
# difference = set1 - set2 
# print(difference)
# print(set1 > set2)
# print(set1 < set2)
# print(list(set1)) #can convert set to list using list constructor
# set4 = {"Roger", "Syd", "Aika", "Roger"}
# print(len(set4)) #set contains only unique values

# # Functions 

# def hello(name = "my friend", age = 30): # now argument is optional, because it has default value 
#     print("Hello " + name + ", you are " + str(age) + " years old")

# hello("Ben", 31)

# def change(val): 
#     val = 2
# val = 1 # this parameter is immutable
# change(val) #doesn't affect the val outside the function
# print(val)

# def change2(val): 
#     val["name"] = "Syd"
# val2 = {"name": "Bow"} # dictionary is mutable
# change2(val2) #affects the val outside the function
# print(val2)

# def talk(phrase): 
#     def say(word): #nested function, bcs we don't want to use it outside the talk fn
#         print(word)
    
#     words = phrase.split(' ') #splits phrase into separate words by space
#     for word in words: 
#         say(word)

# talk("I am going to buy the milk")

# def count(): 
#     count = 0 #not global variable bcs it's inside a fn 

#     def increment(): 
#         nonlocal count #need to specify "nonlocal" to be able to access a variable outside this function
#         count += 1
#         print(count)

#     increment()

# count()

# # Closures
# def counter(): 
#     count = 0 

#     def increment(): 
#         nonlocal count
#         count += 1
#         return count 
    
#     return increment

# increment = counter()

# print(increment()) # = 1
# print(increment()) # = 2 (bcs it will not reset count to 0 again, it has access to the state of count variable)
# print(increment()) # = 3

# # Objects (everything in python is object, dictionaries, integers, lists, tuples, etc, and objects have attributes and methods)

# age = 8 #int object
# print(age.real)
# print(age.bit_length())
# items = [1, 2]
# items.append(3)
# items.pop()
# print(id(items)) #id is location in memory
# age += 1 #not same object anymore, but dictionary will remain same object

# #Loops

# condition = True
# while condition == True: 
#     print("The condition is true")
#     condition = False # will run one time, if didn't set to False it would keep running forever 

# count = 0
# while count < 10: 
#     print("The condition is True")
#     count += 1

# print("After the loop")

# items = [1, 2, 3, 4]
#  item in items: 
#     print(item)

# for item in range(15): # range(15) returns values from 0 to 14 
#     print(item)

# names = ["beua", "syd", "quincy"]

# for index, item in enumerate(names): # enumerate returns indices and items 
#     print(index, item)

# for item in items: 
#     if item ==2: 
#         continue #skips when item is 2
#     print(item)

# for item in items: 
#     if item ==2: #stops when item is 2
#         break
#     print(item)

# # Classes 
# #from Classes you can instanciate objects

# class Animal:
#     def walk(self): 
#         print("walking...")

# class Dog(Animal): #dog inherits Animal methods
#     #constructor, to initialise some properties 
#     def __init__(self, name, age): 
#         self.name = name
#         self.age = age

#     def bark(self): 
#         print("woof!")

# roger = Dog("Roger", 8)

# print(type(roger))
# print(roger.name)
# print(roger.age)

# roger.bark()
# roger.walk()

# Modules 

#  every python file is a module, you can import modules from other files
# if you have file dog.py which has a method bark, you can either 
# import dog (to import all) and then call dog.bark()
# from dog import bark (just pick fns you need) and directly call bark() 
# if dog.py is in subfolder, you need to create another 
# file __init__.py in that folder to define all modules that can be imported 
# and then call from foldername.dog import bark

# # Accepting Arguments in console/shell/terminal

# # import sys

# # name = sys.argv[1]

# # print(sys.argv)
# # print(f"Hello {name}")

# import argparse

# parser = argparse.ArgumentParser(
#     description="this program prints the name of my dogs"
# )

# parser.add_argument('-c', '--color', metavar='color', required=True, choices={'red', 'yellow'}, help='the color to search for')
# # ptyhon main.py -c red, it returns red  
# args = parser.parse_args()

# print(args.color)

# # Lambda functions

# lambda num : num * 2 # lambda arg : expression 

# multiply = lambda a, b : a * b # 2 args, assigned to multiply var 

# print(multiply(2, 4))

#  # map, filter, reduce

# numbers = [1, 2, 3, 4, 5, 6]
# # map passes each number in a list to a function
# # the original list doesn't change
# print(list(map(lambda a: a*2, numbers) ))

# #returns only list which is true
# print(list(filter(lambda a: a%2==0, numbers)))

# from functools import reduce
# expenses = [
#     ('Dinner', 80), 
#     ('Car repair', 120)
# ]
# # a is previous cumulated value, b is new value 
# sum = reduce(lambda a, b: a[1] + b[1], expenses)

# print(sum)


# # Recursion

# def factorial(n): 
#     #define when to get out of recursive to stop recursion
#     if n == 1: return 1
#     return n* factorial(n-1)

# print(factorial(4))

# # Decorators 
# # to change the way the function works without modifying the fn itself
# # or when you need to run the same fn on multiple functions 

# def logtime(func): 
#     def wrapper(): 
#         # do something before 
#         print("before")

#         val = func()

#         # do something after
#         print("after")

#         return val 
#     return wrapper

# @logtime #whenever hello fn is called the logtime decorator 
# def hello(): 
#     print('hello')

# hello()

# # Docstrings

# """Dog module 

# This module does ... and provides the 
# following classes: 

# - Dog
# ...

# """
# def increment(n):
#     """Increment a number""" # describing a function 
#     return n + 1

# class Dog: 
#     """A class representing a dog""" # class docstring 
#     def __init__(self, name, age):
#         """Initialize a new dog"""
#         self.name = name
#         self.age = age 

#     def bark(self): 
#         """Lets the dog bark"""
#         print("Wof!")

# print(help(Dog))

# # Annotations

# def increment(n: int) -> int: 
#     return n + 1

# count: int = 0 # but python ignores the types, doesn't check for types

# # List compressions

# numbers = [1, 2, 3, 4, 5]

# numbers_power_2 = [n**2 for n in numbers]
# print(numbers_power_2)
