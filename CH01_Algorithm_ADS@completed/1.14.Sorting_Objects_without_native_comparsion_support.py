from operator import attrgetter
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __repr__(self):
        return "User({})".format(self.user_id)

users = [User(90), User(10), User(60)]
print(users)
users.sort(key=attrgetter("user_id"))
#attrgetter("attr1", "attr2", ...)
# same with min, max
print(users)
