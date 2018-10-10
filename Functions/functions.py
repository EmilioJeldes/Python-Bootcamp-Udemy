# Syntax
# def name_function():
#   block of runnable code


def sing_happy_birthday():
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")
    print("Happy Birthday to you!")


def square_seven():
    return 7 * 7


def square(num):
    return num * num


def add(a, b):
    return a + b


def substract(a, b):
    return a - b


# can pass default params to a function, including another one
def math(a, b, fn = add):
    """function comment"""
    return fn(a, b)


# global
# word to change a variable that's outside the function
# If only want to access a global variable, there's no need to use global


# nonlocal
# Lets us modify a parent's variables  in a child (aka nested) function

# *args (any name, conventionally is args
# unlimited arguments and it gives a tuple
def sum_all_nums(*args):
    total = 0
    for arg in args:
        total += arg
    return total


# **kwargs (any name)
# same as *args but stores in a dictionary


# Parameter Order
# 1. parameters
# 2. *args
# 3. default parameters
# 4. **kwargs
def display_info(a, b, *args, instructor = "Colt", **kwargs):
    return [a, b, args, instructor, kwargs]


# Unpacking params
# *(tuple) or *[list]
nums = [1, 2, 3, 4, 5, 6]
print(sum_all_nums(*nums))

sing_happy_birthday()
print(square_seven())
print(square(4))
print(math(2, 3))
print(math(2, 3, substract))
print(math(b = 2, a = 2))
print(sum_all_nums(4, 5, 6, 7, 8))
print(display_info(1, 2, 3, last_name = "Steele", job = "Instructor"))
