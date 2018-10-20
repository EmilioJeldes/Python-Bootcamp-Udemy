# Handle errors

# Try-catch python version
# try:
#     block of code to be executed
# except NameError as err:
#     handle the error

try:
    foobar
except NameError as err:
    print(err)

print("After err")


# Handle multiple Errors
def divide(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print("Cant divide by 0")
    except TypeError as err:
        print("a and b must be ints or floats")
        print(err)
    else:
        print(f"{a} divided by {b} is = {result}")


divide(5, 5)
divide("asd", 6)  # a and b must be ints or floats

# For every error
# Not a good practice
try:
    foobar
except:
    print("Something went wrong")

# try, except, else, finally
try:
    # Tries to execute this code
    num = int(input("Insert a number"))
except:
    # If errors are found this gets executed
    print("That is not a number")
else:
    # If no error are found, this part gets executed
    print("This will run if no errors are found")
finally:
    # This will always be executed
    print("This will always run, no matter what")
