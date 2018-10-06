# An ordered collection or grouping of items
# IMMUTABLE

# Syntax
numbers = (1, 2, 3, 4, 5)
names = tuple(("Carlos", "Juan", "Pedro"))
# numbers[0] = 4 CANT BE DONE
contains = 3 in numbers  # TRUE

# Tuples can be used as keys in dictionaries
locations = {
    (35.6895, 39.6917): "Tokyo Office",
    (40.7128, 74.0060): "New York Office",
    (37.7749, 122.4194): "San Francisco Office"
}

# .count(x)
# counts how many times x is contained in the tuple
numbers.count(1)

# .index(x)
# Returns the index at wich a value is found in a tuple
# Only the first matching
numbers.index(5)
