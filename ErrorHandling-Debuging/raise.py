# raise
# To throw a custom error or exception
# raise ValueError('Invalid value')


def colorize(text, color):
    if type(text) is not str:
        raise TypeError("text must be an instance of str")
    print(f"Printed {text} in {color}")


print(colorize("hello", "red"))
print(colorize(32, "red"))  # throws TypeError
