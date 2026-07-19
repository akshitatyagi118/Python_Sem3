# Advanced Python Concepts

# Decorator
def my_decorator(func):
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper

@my_decorator
def say_hello():
    print("Hello!")
say_hello()
# Output:
#Something is happening before the function is called.
#Hello!
#Something is happening after the function is called.


# Generator
def countdown(n):
    while n > 0:
        yield n
        n -= 1
# Using the generator
for num in countdown(5):
    print(num)  
# Output:
#5 
#4 
#3 
#2 
#1


# Closure
def outer_func(x):
    def inner_func(y):
        return x + y
    return inner_func
add_five = outer_func(5)
print(add_five(3)) 
# Output: 8