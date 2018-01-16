from random import randint

class User(object):

    def __init__(self, username="", password="", email=""):
        self.username = username
        self.password = password
        self.email = email

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")

    @classmethod
    def random(cls):
        password_rnd="pass" + str(randint(0, 1000000));
        return cls(username="user" + str(randint(0, 1000000)),
                   password=password_rnd,
                   email="user" + str(randint(0, 1000000)) + "@test.com");