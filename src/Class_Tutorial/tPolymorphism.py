class Animal:
    def sound(self):
        print("Some generic animal sound")

class Dog(Animal):
    def sound(self):
        print("Bark")

class Cat(Animal):
    def sound(self):
        print("Meow")

# Example usage
animals = [Dog(), Cat(), Animal()]
for a in animals:
    a.sound()  # Each object responds differently
