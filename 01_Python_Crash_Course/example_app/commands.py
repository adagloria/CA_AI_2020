from api import User

user = User()
commands = dict(get=user.get, put=user.put, post=user.post, delete=user.delete)
