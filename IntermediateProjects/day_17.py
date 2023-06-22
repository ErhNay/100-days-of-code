# Benefits of Object Oriented Programming
# My First Class
class User:
    
    # def __init__(self, user_id, user_name):
    #     self.id = user_id
    #     self.name = user_name
        
    #     print(self.id)
    #     print(self.name)
    
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.name = user_name
        self.followers = 0
        self.following = 0
        # self. arr = [1,12,2,568,898,989,56,56]
        # self.dic = {"name": "X-men", "sex":"male"}
        
        
    def follow(self, user):
        user.followers += 1
        self.following += 1
        
        


user1 = User("25", "Norbie Amanks")
user2 = User("60", "Norbie Amanks")

user1.follow(user2)

print(user1.followers)
print(user1.following)
print(user2.followers)
print(user2.following)