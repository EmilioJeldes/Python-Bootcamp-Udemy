# Error Handling and Debbuging

## Common Errors

### Name Errors
This occurs when a variable is not defined, i.e. it hasn't been assigned

### Type Error
An operation or function is applied to the wrong type

### Index Error

### Value Error
This occurs when a built in operation or function receives an argument that has the right type
but an inappropriate value

### Key Error
This occurs when a dictionary does not have a specific key

### Attribute error
This occurs when a variable does not have an attribute

## Create Custom Errors
### `raise`
To throw a custom error or exception
````python
raise ValueError('Invalid value')

def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be an instance of str")
    print(f"Printed {text} in {color}")


print(colorize("hello", "red"))
print(colorize(32, "red"))  # throws TypeError
````

## Handle errors
### Syntax
`````python
# Try-catch python version

try:
    # block of code to be executed
except NameError as err:
    # handle the error
`````

### Handle multiple Errors
Multiple except statements
`````python
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
`````

### For every error
_**Not a good practice**_
`````python
try:
    foobar
except:
    print("Something went wrong")
`````

### try, except, else, finally
`````python
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
`````


