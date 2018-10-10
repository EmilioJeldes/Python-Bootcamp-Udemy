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


print(User.display_active_users())
user = User.from_string("Emilio, Jeldes, 28")
print(user.full_name())
