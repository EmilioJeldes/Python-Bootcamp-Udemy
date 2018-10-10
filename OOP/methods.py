class User:
    # class attribute
    # Can me access across all instances of the class with User.active_users
    active_users = 0
    
    # self always on methods
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        self.age = age
        User.active_users += 1
    
    def full_name(self):
        return f"{self.first} {self.last}"
    
    def initials(self):
        return f"{self.first[0]}.{self.last[0]}."
    
    def likes(self, thing):
        return f"{self.first} likes {thing}"
    
    def is_senior(self):
        return self.age > 65
    
    def birthday(self):
        self.age += 1
        return f"Happy {self.age}th, {self.first}"
    
    def logout(self):
        User.active_users -= 1
        return f"{self.first} has logged out"


# print(user1.full_name())
# print(user1.initials())
# print(user2.likes("Chips"))
# print(user2.is_senior())
#
# print(user2.birthday())
# print(user2.birthday())

print(User.active_users)

user1 = User("Emilio", "Jeldes", 28)
user2 = User("Juan", "Perez", 28)
print(User.active_users)
