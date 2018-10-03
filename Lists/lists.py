tasks = ["Install Python", "Learn Python", "Take a break"]
numberList = list(range(1, 4))

# len() to get lenght of the list
print(len(tasks))
print(numberList)

# Ask for a value in a list
print("Install Python" in tasks)

colors = ["Teal", "Magenta", "Purple"]

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

# Remove first match of x
colors.remove("Red")
print(colors)
