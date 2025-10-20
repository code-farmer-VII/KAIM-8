for i in range(5):
    print("Hello, World!")
print("Finished printing greetings.")


def add(a,b):
    return a+ b

result = add(3,5)
print("This is the sum of 3 and 5:",result)

even = [n for n in range(10) if n%2 == 0]
print("Even numbers from 0 to 9:", even)

user, pts = "Bob", 85
print(f"{user} scored {pts}%")  # Bob scored 85%


use = input("Enter something: ")
print("You entered:", use)

age = input("Enter your age: ")
print("Your age is:", age)

name, age = use, age

print(f"my name is {name} and I am {age} years old")


import json

data = { "name":"Temesgen", "skills":["Python","ML","AI", "React", "Laravel"], "age":30 }
#how to write json data to a file
with open("info.json", "w") as file:
    json.dump(data, file, indent=4)
#how to read all of the json data 

with open("info.json", "r") as file:
    content = json.load(file)
    print(content)

#how to write some text data to a file 
with open("notes.txt", "w") as file:
    file.write("This is a sample note.\n")
    file.write("This note is for demonstration purposes.\n")

# how to read all of the text data from a file
with open("notes.txt", "r") as file:
    text_content = file.read()
    print(text_content)
    

class Laptop:
    def __init__(self, brand, ram, storage):
        self.brand = brand
        self.ram = ram
        self.storage = storage

    def specs(self):
        return f"{self.brand} Laptop with {self.ram}GB RAM and {self.storage}GB Storage"
    
class SmartPhone:
    def __init__(self,ram,storage,battery):
        self.ram = ram
        self.storage = storage
        self.battery = battery
    def buy(self):
        return f"Buying a smart phone with {self.ram}GB RAM, {self.storage}GB Storage, and {self.battery}mAh Battery"
