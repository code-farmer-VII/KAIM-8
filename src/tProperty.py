#creating a propery in class 

class Person:
    def __init__(self,name):
        self._name = name  # private attribute
    @property
    def name(self):
        return self._name
    @name.setter
    def name(self, name):
        self._name = name   
# Example usage
person = Person("Temesgen")
print(person.name)  # Access through property
