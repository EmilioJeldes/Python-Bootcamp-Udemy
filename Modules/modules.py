# Imports
# When you use import, Python...
# 1. Tries to find the module (if it fails, throws an error
# 2. Runs the code inside of the module being imported

# __name__
# inside the main running file, __name__ is equal to __main__
# if __name__ == '__main__':
# it only executes code if the file is the actual running file


# Build in examples

import random

fruits = ["apple", "banana", "cherry", "durian"]
print(random.choice(fruits))
print(random.shuffle(fruits))

# Alias to a module
import random as my_custom_alias

print(my_custom_alias.choice(fruits))

# Import parts of a module
# The key "from" lets you import part of a module
from random import choice

print(choice(fruits))

# Custom Module
import custom_module

print(custom_module.fn())

from custom_module import other_fn as f

print(f())
