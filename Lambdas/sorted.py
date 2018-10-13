# sorted(iterable, reverse=boolean, key=function)
# reverse and key argument are not mandatory
# key can be a built in function like len or a lambda
# Can accept a tuple
# Returns a new sorted list from the items in iterable
# It's a copy, it does not modify the original iterable

nums = [94, 49, 2, 6, 6, 7, 1]
nums2 = sorted(nums)

print(nums)
print(nums2)
print(nums)

users = [
    {"username": "Samuel", "tweets": ["I love cake", "I love cookies"], "color": "purple"},
    {"username": "Katie", "tweets": ["I love my cat"], "number": 46, "color": "purple"},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

# it orders by length
print(sorted(users, key = len))

# it orders each user by username value
print(sorted(users, key = lambda user: user["username"]))
