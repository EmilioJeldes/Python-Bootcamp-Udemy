class Aquatic:
    
    def __init__(self, name):
        print("AQUATIC INIT")
        self.name = name
    
    def swim(self):
        return f"{self.name} is swimming"
    
    def greet(self):
        return f"I am {self.name} of the sea"


class Ambulatory:
    
    def __init__(self, name):
        print("AMBULATORY INIT")
        self.name = name
    
    def walk(self):
        return f"{self.name} is walking"
    
    def greet(self):
        return f"I am {self.name} of the land"


class Penguin(Ambulatory, Aquatic):
    
    def __init__(self, name):
        print("PENGUIN INIT")
        # Only first one gets called
        # super().__init__(name = name)
        # Both constructors gets called
        Ambulatory.__init__(self, name = name)
        Aquatic.__init__(self, name = name)


jaws = Penguin("Jaws")
print(jaws.swim())
print(jaws.walk())
print(jaws.greet())
