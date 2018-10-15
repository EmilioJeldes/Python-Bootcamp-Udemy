# filter(function, iterable)
# returns a filter object of the original collection
# can be turned into a iterator

num_list = [1, 2, 3, 4, 5, 6]

evens = list(filter(lambda x: x % 2 == 0, num_list))

print(evens)

users = [
    {"username": "Samuel", "tweets": ["I love cake", "I love cookies"]},
    {"username": "Katie", "tweets": ["I love my cat"]},
    {"username": "Jeff", "tweets": []},
    {"username": "Bob123", "tweets": []},
    {"username": "doggo_luvr", "tweets": ["dogs are the best"]},
    {"username": "guitar_gal", "tweets": []}
]

# FILTER AND MAP TOGETHER
filtered_mapped = list(map(lambda user: user["username"].upper(),
                           filter(lambda u: not u["tweets"], users)))

print(filtered_mapped)

# Same as above
filtered_mapped_list_comp = [user["username"].upper() for user in users if not user["tweets"]]

print(filtered_mapped_list_comp)
