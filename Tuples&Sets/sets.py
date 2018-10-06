# Syntax
# Cannot have duplicates
s = set({1, 2, 3, 4, 5, 6, 6})
se = {1, 2, 3, 4, 5, 6, 6}
# {1, 2, 3, 4, 5, 6}

# 4 in s => Tue
# 10 in s => False

# add elements
# .add(x) if x is already in, it doesnt change
s.add(7)

# remove value from set
# .remove(x) Return KeyError if the value is not found
# .discard(x) it does not return errors
s.remove(6)

# Copy the set
# .copy()
# Not the same object, but a copy of the values
e = s.copy()

# Remove everyting
# clear()
e.clear()

# UNION SET
# | pipe to unit sets (sets)
# & returns match values
math_students = {"Matthew", "Helen", "Prashant", "James", "Aparna"}
biology_students = {"Jane", "Matthew", "Charlotte", "Mesut", "Oliver", "James"}


all_students = math_students | biology_students
print(all_students)

matched_students = math_students & biology_students
print(matched_students)
