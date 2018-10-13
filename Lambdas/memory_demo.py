import sys

list_comp = sys.getsizeof([x * 10 for x in range(100)])
gen_exp = sys.getsizeof(x * 10 for x in range(1000000000))

print("Do the same thing it takes:")
print(f"List Comprehension: {list_comp} bytes")
print(f"Generator Expression: {gen_exp} bytes")
