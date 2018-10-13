# map(function, iterator)
# Iterates over an iterator and executes a function
# returns a map object and it needs to be casted into something usefull like a list
# stored variable of a map, can only be used once (must be casted to preserved it)

nums = [1, 2, 3, 4, 5, 6]
doubles = map(lambda x: x * 2, nums)
print(doubles)

# needs to be casted to access the values
doubles = list(map(lambda x: x * 2, nums))
print(doubles)

# Useful use case
names = [
    {"first": "Rusty", "last": "Steele"},
    {"first": "Colt", "last": "Steele"},
    {"first": "Blue", "last": "Steele"},
]

first_names = list(map(lambda value: value["first"], names))

print(first_names)
