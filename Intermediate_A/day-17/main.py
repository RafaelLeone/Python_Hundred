class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
        print("User being created...")

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User(1, "Angela")
user_2 = User(2, "Jacfdk")

user_1.follow(user_2)

print("User 1:\nFollowers: " + str(user_1.followers))
print("       \nFollowing: " + str(user_1.following) + "\n")
print("User 2:\nFollowers: " + str(user_2.followers))
print("       \nFollowing: " + str(user_2.following) + "\n")
