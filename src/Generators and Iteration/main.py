#Generators and Iteration
def simple_generator():
    yield 1
    yield 2
    yield 3

for value in simple_generator():
    print(value)
# Example of using a generator expression
squares = (x*x for x in range(5))
for square in squares:
    print(square)

# Example of using itertools for iteration
import itertools
numbers = [1, 2, 3, 4, 5]
pairs = itertools.combinations(numbers, 2)
for pair in pairs:
    print(pair)

# Example of a simple generator function
def count_up_to(n):
    count = 1
    while count <= n:
        yield count   # pauses and returns a value
        count += 1

# Using the generator
for number in count_up_to(5):
    print(number)

    # return   Ends the function and sends one value           ->    Regular functions      
    # yield    Pauses the function and sends a sequence of values  -> Generators (iteration) 

print("Using next() with the generator:")
gen = count_up_to(3)
print(next(gen))  # 1
print(next(gen))  # 2
print(next(gen))  # 3
# next(gen) -> StopIteration

print("Using next() with the generator: to iterate even numbers")
def even_numbers():
    n = 0
    while True:
        yield n
        n += 2

gen = even_numbers()
for _ in range(5):
    print(next(gen))
