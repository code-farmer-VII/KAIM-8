class Bird:
    def fly(self):
        print("Bird is flying")

class Airplane:
    def fly(self):
        print("Airplane is flying")

def start_flying(entity):
    entity.fly()  # Works as long as entity has a fly() method

start_flying(Bird())
start_flying(Airplane())
