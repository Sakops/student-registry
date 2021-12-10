from dataclasses import dataclass
import json
#classes and objects
class User: #how to create a class
    name: str
    salary: int
    def __init__(self,name, salary):
        self.name = name
        self.salary = 300
user1 = User("Sam", 2000)

print(user1.__dict__)

@dataclass
class Square: 
    a: int
    b: int
    def perimeter(self): 
        return (self.a+self.b)*2
    
square = Square(2,3)
print(square.perimeter())

#type hinting
def perimeter(a: int, b: int) -> int: 
    """This is a perimeter function""" #saying what function does
    return (a+b) *2

perimeter(4,4)

#function that sum many nums a once
def sumAll(*nums):
    result = 0
    for num in nums:
        result += num
    return result

print(sumAll(32,3,4,3,5))

#kwargs
def makeDict(**kwargs): #creates a dictionary
    print(kwargs)

makeDict(name= "sam", job= "programmer")

#reading files

f = open("test.txt", "a")
f.write("asdfasd")
f.close()

class User: 
    name: str
    salary: int

user = User()
user.name = "someone"
user.salary = None
user_json = json.dumps(user.__dict__)
print(user_json)
with open("user_json", "w") as f: #creating json file
    json.dump(user.__dict__,f)