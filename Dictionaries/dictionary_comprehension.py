numbers = dict(first = 1, second = 2, third = 3)

# Syntax
# { __ : __  for __  in __}
# {key : val for val in list}
squared_numbers = {key: value * 3 for key, value in numbers.items()}
# {'first': 3, 'second': 6, 'third': 9}

nums_from_list = {num: num ** 2 for num in [1, 2, 3, 4, 5]}
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}


string1 = "ABC"
string2 = "123"

combo = {string1[i]: string2[i] for i in range(len(string1))}
# {'A': '1', 'B': '2', 'C': '3'}

instructor = dict(name = "Colt", city = "San Francisco", color = "Purple")
yelling_instructor = {k.upper(): v.upper() for k, v in instructor.items()}
# {'NAME': 'COLT', 'CITY': 'SAN FRANCISCO', 'COLOR': 'PURPLE'}

# CONDITIONALS
even_odd = {num: ("even" if num % 2 == 0 else "odd") for num in [1, 2, 3, 4, 5]}
# {1: 'odd', 2: 'even', 3: 'odd', 4: 'even', 5: 'odd'}

# EXERCISES
# 1
person = [["name", "Jared"], ["job", "Musician"], ["city", "Bern"]]
answer0 = {person[i][0]: person[i][1] for i in range(len(person))}
answer1 = {thing[0]: thing[1] for thing in person}
answer2 = {k: v for k, v in person}
# If you have a list of pairs, you can very easily turn it into a dictionary using dict()
answer3 = dict(person)
print(answer3)

# 2
answer = {char: 0 for char in "aeiou"}
# {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}

# 3
ascii_chars = {i: chr(i) for i in range(65, 91)}
# {65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E', 70: 'F', 71: 'G', 72: 'H', 73: 'I', 74: 'J', 75: 'K', 76: 'L', 77: 'M',
# 78: 'N', 79: 'O', 80: 'P', 81: 'Q', 82: 'R', 83: 'S', 84: 'T', 85: 'U', 86: 'V', 87: 'W', 88: 'X', 89: 'Y', 90: 'Z'}

