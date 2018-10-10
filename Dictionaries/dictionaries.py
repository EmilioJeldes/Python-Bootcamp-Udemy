# syntax
first_dictionary = {"key": "value"}
second_dictionary = dict(key = "value", key2 = "value2")

# Access a property
print(first_dictionary["key"])
print(second_dictionary["key2"])

# Iterate over a dictionary getting all values
# .values()
for val in second_dictionary.values():
    print(val)

# Iterate over a dictionary using the keys
# .keys()
for key in second_dictionary.keys():
    print(second_dictionary[key])

# Iterate over a dictionary getting all key and value as tuple
# .items()
for k, v in second_dictionary.items():
    print(f"Key is {k} and value is {v}")

# Ask for keys in a dictionary (contained)
# "key" in dictionary
print("key" in second_dictionary)

# Ask for values in a dictionary (contained)
# "value" in dictionary.values
print("value" in second_dictionary.values())

# Remove all
# .clear()
d = dict(a = 1, b = 2, c = 3)
d.clear()
print(d)
d = dict(a = 1, b = 2, c = 3)

# Copy elements of a list into a new one
# .copy()
c = d.copy()
print(c)
print(c is d)

# Create from keys
# .fromkeys([keys...], value(s))
user = {}.fromkeys(["name", "lastname", "age", "email"], "unknown")
# {'name': 'unknown', 'lastname': 'unknown', 'age': 'unknown', 'email': 'unknown'}

# Get value from key
# Returns None if nothing it's found
print(second_dictionary.get("key2"))

# Remove specific key item
# .pop(x) x = keyElement. Cant be passed without argument
# Returns a KeyError if no element is found or if passed empty
print(user.pop("name"))

# Remove randomly an item from dict
# .popitem()
print(user.popitem())

# Adds a dictionary to another (like concat). Do not remove anything, just adds
# .update(list)
second_dictionary.update(user)
print(second_dictionary)

# Add new value
second_dictionary["new_value"] = "value"

# Unpacling Dictionaries
# **dictionary_name
