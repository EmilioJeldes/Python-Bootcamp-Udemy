# Lambdas & Built in Functions
Syntax for lambdas and built in functions

## Lambda
`````python
square = lambda x: x * x
`````

## Build in Functions
### 1. ``map(function, iterable)``
Iterates over an iterable and executes a function.
Returns a map object and it needs to be casted into something usefull like a list.
Stored variable of a map, can only be used once (must be casted to preserved it)
`````python
# Executes the lambda function for every item of the given iterable

doubles = map(lambda x: x * 2, nums)
first_names = list(map(lambda value: value["first"], names))
`````

### 2.``filter(function, iterable)``
Returns a filter object of the original collection.
Can be turned into a iterator
`````python
# Filter a list of numbers and just return evens

evens = list(filter(lambda x: x % 2 == 0, num_list))

`````

### 3. ``filter(function, iterable) + map(function, iterable)``
Filter and map together
`````python
# 1. Filter a list of users and return only those with no tweets.
# 2. Then it maps over the returned list and it sets all usernames to uppercase
# 3. Finally it converts the resoult to a list

filtered_mapped = list(map(lambda user: user["username"].upper(),
                           filter(lambda u: not u["tweets"], users)))
`````

> The same can be done with list comprehension
`````python
filtered_mapped_list_comp = [user["username"].upper() for user in users if not user["tweets"]]
`````

### 4. ``all(iterable)``
Returns True if all elements of the iterable are truthy. Returns false if the iterable is empty
`````python
all(num for num in [2, 4, 6, 8, 10] if num % 2 == 0) 
`````

### 5. ``any(iterable)``
Returns True if any of the elements inside the iterable is a truthy value. If the iterable is empty, returns false
`````python
any([0, 2, 3, 4, 5])  # True, because all except 0 are truthy.
`````

### 6. ``sorted(iterable, reverse=boolean, key=function)``
Reverse and key argument are not mandatory.
Key can be a built in function like len or a lambda. 
Can accept a tuple as iterable. 
Returns a new sorted list from the items in iterable
It's a copy, it does not modify the original iterable
`````python
# it orders each user by username value

print(sorted(users, key = lambda user: user["username"]))
`````

### 7. ``min(iterable, key=function) - max(iterable, key=function)``
Key is not mandatory.
Returns the minimum / maximum value of the iterable.
Can accept a function key as a judge to get the value
`````python
min(names, key = lambda n: len(n))
max(names, key = lambda n: len(n))
`````

### 8. ``reverse(iterable)``
Returns a reverse iterator
`````python
for char in reversed("Hello world"):
    print(char)
`````

### 9. ``abs(n)``
Returns the absolute value of a number.
The number can be a float or an int.
`````python
print(abs(-2.5))  # 2.5
print(abs(-22))   # 22
`````

### 10. ``round(number, ndigits)`` 
Return number rounded to ndigits precision after the decimal point.
If ndigits is omitted or None, it returns the nearest integer
`````python
round(10.4)  # 10
round(1.234567, 2)  # 1.23
`````

### 11. ``zip(iterable, iterable)`` 
Make an iterator that agregate elements from each of the iterables.
Returns an iterator of tuples, where the i'th tuple contains the i'th element from each of the of the argumentsequences or iterables.
The iterator stops when the shortest input iterable is exhausted
`````python
first_zip = zip([1, 2, 3], [4, 5, 6])
print(list(first_zip))  # [(1, 4), (2, 5), (3, 6)]
print(dict(first_zip))  # {1: 4, 2: 5, 3: 6}
`````