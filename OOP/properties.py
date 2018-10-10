class Human:
    
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        # property methods can be passed as a simple property via constructor
        self.age = age
    
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("Age cant be negative")


jane = Human("Jane", "Johnson", 45)
print(jane.age)
# You can still change the private property
jane._age = 60

print(jane.age)
