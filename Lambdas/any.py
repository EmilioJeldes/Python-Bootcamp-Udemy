# any()
# returns True if any of the elements inside the iterable is a truthy value.
# If the iterable is empty, returns false

# THERE'S NO NEED TO USE LIST COMPREHENSION, JUST GENERATOR EXPRESSION
any([0, 2, 3, 4, 5])  # True, because all except 0 are truthy
