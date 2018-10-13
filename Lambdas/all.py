# all(iterable)
# returns True if all elements of the iterable are truthy (or if the iterable is empty)

all([0, 1, 2, 3])  # False, 0 is a Falsy value

# THERE'S NO NEED TO USE LIST COMPREHENSION, JUST GENERATOR EXPRESSION
all([char for char in 'eio' if char in "aeiou"])  # True every character is inside 'aeiou'

all(num for num in [2, 4, 6, 8, 10] if num % 2 == 0)  # True, every numbers is even

people = ["Casey", "Charlie", "Cody", "Carly", "Cristina"]

all(name[0] == "C" for name in people if name[0] == "C")  # True, all values start with C
