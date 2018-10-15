# min(iterable, key=function) - max(iterable, key=function)
# Key is not mandatory.
# Returns the minimum / maximum value of the iterable.
# Can accept a function key as a judge to get the value

num_list = [1, 2, 3, 4, 5, 6]
names = ["Arya", "Tim", "Samson", "Dora", "Ollivander"]

min(num_list)  # Returns 1
max(num_list)  # Returns 6
min(names, key = lambda n: len(n))  # returns Ollivander
max(names, key = lambda n: len(n))  # returns Tim


