class User(object):

    def __init__(self, username=None, password=None, email=None, name=None, year=None):
        self.username = username
        self.password = password
        self.email = email
        self.name = name
        self.year = year

    @classmethod
    def Admin(cls):
        return cls(username="admin", password="admin")

    @classmethod
    def AddFilm(cls):
        return cls(name="Blade Runner", year="1982")

    @classmethod
    def RemoveFilm(cls):
        return cls(name="Gladiator", year="2000")

    @classmethod
    def random(cls):
        from random import randint
        return cls(username="user" + str(randint(0, 1000000)),
                   password="pass" + str(randint(0, 1000000)),
                   email="user" + str(randint(0, 1000000)) + "@test.com")