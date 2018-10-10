class Animal:
    
    def speak(self):
        # Needs to be implemented
        raise NotImplementedError("Subclass needs to implement this error")


class Dog(Animal):
    
    def speak(self):
        return "Woof!"


class Cat(Animal):
    
    def speak(self):
        return "MEOW!"


class Fish(Animal):
    
    def speak(self):
        return "Something"


d = Dog()
print(d.speak())

f = Fish()
print(f.speak())
