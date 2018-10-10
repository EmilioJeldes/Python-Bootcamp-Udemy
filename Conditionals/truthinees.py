x = 1
x is 1  # True
x is 0  # False

# Empty objects, Empty String, None and Zero are naturaly False
string = None
string1 = ""
list = []
dict = {}
zero = 0

print(f"String None {bool(string)}")
print(f"string1 '' {bool(string1)}")
print(f"Empty List {bool(list)}")
print(f"Empy dict {bool(dict)}")
print(f"Integer 0 {bool(zero)}")