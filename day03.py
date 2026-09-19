# def greet():
#     print("Hello, welcome to the program!")

#name is parameter
#Alice is argument
def greet(name):
    print(f"hello {name}, welcome to the program!")

greet("Alice")  

def add(a, b):
    """returns the sum of two numbers"""
    return a + b

print(add.__doc__)