# Opening files

# write()
# Still have to open the file and then use the method write()

with open("haiku.txt", "w") as file:
    file.write("Writing files is great\n")
    file.write("Here's another line of text\n")
    file.write("Closing now, Bye!")

with open("haiku.txt") as file:
    data = file.read()

print(data)
