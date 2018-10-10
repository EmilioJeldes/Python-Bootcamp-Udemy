class User:
    # class attribute
    active_users = 0
    
    # Shared by all User instances
    @classmethod
    def display_active_users(cls):
        return f"There are currently {cls.active_users} active users"
    
    @classmethod
    def from_string(cls, string_data):
        first, last, age = string_data.split(",")
        return cls(first, last, int(age))
    
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


class Moderator(User):
    # total mods
    total_mods = 0
    
    @classmethod
    def display_active_mods(cls):
        return f"There are currently {cls.total_mods} active users"
    
    def __init__(self, first, last, age, comunity):
        super().__init__(first, last, age)
        self.comunity = comunity
        Moderator.total_mods += 1
    
    def remove_post(self):
        return f"{self.full_name()} removed a post from {self.comunity} comunity"


u1 = User("Tom", "Garcia", 35)
u2 = User("Tom", "Garcia", 35)
u3 = User("Tom", "Garcia", 35)
jasmine = Moderator("Jasmine", "O'conell", 61, "Piano")
jasmin2 = Moderator("Jasmine", "O'conell", 61, "Piano")
print(jasmine.full_name())
print(jasmine.comunity)

print(User.display_active_users())
print(Moderator.display_active_mods())