#this code shows how to use Magic and methods in python classes

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def __str__(self):
        return f"User(name={self.name}, email={self.email})"
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"
    def __eq__(self, other):        
        return self.email == other.email        
    def __len__(self):
        return len(self.name)    
    def __add__(self, other):
        if isinstance(other, User):
            return User(self.name + " & " + other.name, self.email + "; " + other.email)
        return NotImplemented
# Example usage
user1 = User("Temesgen", "   2M2i8@example.com")            
user2 = User("Alice", "   2M2i8@example.com")       
print(user1)  # Uses __str__
print(repr(user2))  # Uses __repr__ 
print(user1 == user2)  # Uses __eq__
print(len(user1))  # Uses __len__
print(user1 + user2)  # Uses __add__



