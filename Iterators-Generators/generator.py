# A generator is returned by a generator function
# Instead of return it yields (return | yield)
# Can be return multiple times, not just 1 like in a normal function


def count_up_to(max_val):
    count = 1
    while count <= max_val:
        yield count
        count += 1


# counter now is a generator and i can call the method next(counter)
counter = count_up_to(5)

for i in count_up_to(5):
    print(i)
