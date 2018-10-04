tasks = ["Install Python", "Learn Python", "Take a break"]
numberList = list(range(1, 4))

# len() to get lenght of the list
print(len(tasks))
print(numberList)

# Ask for a value in a list
print("Install Python" in tasks)

colors = ["Teal", "Magenta", "Purple", "Magenta"]

# Cover a list
for color in colors:
    print(color)

# Add item at the end
colors.append("Red")

# Adds another list at the end of the current list
colors.extend(["Blue", "Yellow"])
print(colors)

# Inserts an item into a given position
colors.insert(0, "Black")
print(colors)

# Remove all items
tasks.clear()

# Remove specific item out of the list
# If no arguments are passed in, by default removes the last one
colors.pop(0)
colors.pop()
print(colors)

# Remove first match of x. Does not return the item like .pop()
colors.remove("Red")
print(colors)

# .index(x, start_index, end_index) Gives back the index of the x contained on the list
print(colors.index("Magenta"))
print(colors.index("Magenta", 2, 4))

# .count(x) counts the times the x element is contained on the list
print(colors.count("Magenta"))

# .reverse() reverse the order of the list in place. It doesnt return anything so you cant print it right away
colors.reverse()
print(colors)

# .sort() sort the items on the list in a ascending way.
# Same as .reverse(), it doesn't return anything so you cant print it right away.
colors.sort()
print(colors)

# .join(x) is used on a string and the x element is the list.
# It concatenates every element of the list with the string on that is used .join(x)
# It does not modify the list
print(" ".join(colors))

# Slice
# list[start:end:step]
# start = start index (including it). Can me without setting it and it will mean that starts from 0
# end = end index NOT INCLUDED. If is missing it will count as the rest of the list
print(colors[1:])
print(colors[0: 2])
print(colors[0: 4: 1])
print(colors[-1:])
print(colors[-3:])
print(colors[:1])

# Swapping values
# Use a "coma" and reasign the values
print(colors)
colors[0], colors[1] = colors[1], colors[0]
print(colors)

