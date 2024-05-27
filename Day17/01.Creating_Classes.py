# Creating a Class

# a class named User, use the __init__() function to assign values for User Id and Username.
class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        
user1 = User("001", "NEMESIS")
user2 = User("002", "Birendra")

print(user1.id)
print(user1.username)

# Adding Methods

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
user1 = User("001", "NEMESIS")
user2 = User("002", "Birendra")

user1.follow(user2)

print(f"{user1.username} is following {user1.following}")
print(f"{user1.username} has {user1.following} followers")