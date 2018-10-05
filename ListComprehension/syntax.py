nums = [1, 2, 3, 4, 5, 6]

# [do_something_to_each_variable for variable in list]
new_nums = [x * 2 for x in nums]

print(new_nums)

# Can have conditional logic
# [do_something_to_each_variable for variable in list if_statement]
evens_multiplied = [x * 2 for x in nums if x % 2 == 0]

print(evens_multiplied)

# Can have if else statement
# [do_something_to_each_variable if_else_statement for variable in list]
odds_or_0 = [x if x % 2 != 0 else 0 for x in nums]
print(odds_or_0)

with_vowels = "This is so much fun"
print(" ".join([char for char in with_vowels if char not in "aeiou"]))
