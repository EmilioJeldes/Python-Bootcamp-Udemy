# Iterator = object that can be iterated upon. An object which returns data, one element at a time hen next() is
# called on it

# Iterable = object which will return an iterator when iter() is called

# Lists, Tuples, string, etc are iterable. A for loup calls iter() on the object and on each time it calls next()

# next(iterator) continues until StopIteration error pops up

# ex: hello = "hello"
# it = iter(hello)
# next(it) -> h
# next(it) -> e
# next(it) -> l
# next(it) -> l
# next(it) -> o
# next(it) -> StopIteration


class Counter:
    
    def __init__(self, low, high):
        self.current = low
        self.high = high
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.current < self.high:
            num = self.current
            self.current += 1
            return num
        raise StopIteration


for i in Counter(0, 10):
    print(i)
