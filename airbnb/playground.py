# from datetime import time
#
#
# def decorator(fn):
#     def wrapper(*args, **kwargs):
#         print("i am decorating you")
#         fn(*args, **kwargs)
#         print("Okay bye")
#     return wrapper
#
#
#
# def timer(fn):
#     def inner_function(*args, **kwargs):
#         start = time.time()
#         fn(*args, **kwargs)
#         total_time = time.time() - start
#         print(f"You took {total_time} seconds to run")
#     return inner_function()

# @decorator
# def square(a: int):
#     print(a * a)


class Playground:
    def __init__(self, first_name, last_name, age):
        self._age = age
        self._name = f"{first_name} {last_name}"

    @property
    def name(self):
        print("I am getting name")
        return self._name

    @name.setter
    def name(self, fullname):
        print("i am setting name")
        self._name = fullname

    @property
    def age(self):
        print("I am getting age")
        return self._age

    @age.setter
    def age(self, age):
        if age < 0:
            raise ValueError("Age cannot be nagative")
        self._age = age


p1 = Playground("Funmi", "Bob", 78)
print(p1.name)
