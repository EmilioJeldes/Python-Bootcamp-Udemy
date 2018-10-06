# Syntax
# Same as dictionaries but without a key
# {__ for __ in __}
numbers = {x ** 2 for x in range(10)}
# {0, 1, 64, 4, 36, 9, 16, 49, 81, 25}

set_chars = {char.upper() for char in "Hello"}
# {'L', 'O', 'H', 'E'}

string_value = "sequoia"
contained = len({char for char in string_value if char in "aeiou"}) == 5
# {'u', 'o', 'e', 'a', 'i'}
print(contained)