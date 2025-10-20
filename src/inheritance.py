class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")

# Student inherits from Person
class Student(Person):
    def __init__(self, name, age, student_id):
        super().__init__(name, age)  # call parent constructor
        self.student_id = student_id

    def study(self):
        print(f"{self.name} is studying.")

# Example usage
student1 = Student("Temesgen", 21, "S123")
student1.introduce()  # from parent class
student1.study()      # from child class
