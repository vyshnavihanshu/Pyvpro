class Profile:
    def __init__(self,username):
        self.followers = 0
        self.username = ("_vyshu_123")
    def follow(self):
        print("someone followed you")
        self.followers += 1
    def username_edit(self,new):
        print("you are editing")
        self.username = new
p1 = Profile("_mshgh_ak_")
p1.follow()
print(p1.followers)
print(p1.username)