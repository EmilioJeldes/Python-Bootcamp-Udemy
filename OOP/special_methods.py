from copy import copy


class Human:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
    
    def __repr__(self):
        return f"Human named {self.first} {self.last} aged {self.age}"
    
    def __len__(self):
        return self.age
    
    def __add__(self, other):
        if isinstance(other, Human):
            return Human("Newborn", self.last, 0)
        raise TypeError(f"{other} can't be added to Human")
    
    def __mul__(self, other):
        if isinstance(other, int):
            # self by himself points to the same object in memory so if you change 1, they will all change
            # It needs to be a copy so you can create new Human evey time or import module copy
            return [copy(self) for i in range(other)]
        raise TypeError(f"{other} must be type int")


j = Human("Jenny", "Larson", 47)
k = Human("Kevin", "Jones", 49)
# print(j)
# print(len(j))
# print(k + j)
#
# triplets = k * 3
# triplets[1].first = 'Jessica'
# print(triplets)

triplets = (k + j) * 3
print(triplets)
