class Film(object):

    def __init__(self, name="", year=""):
        self.name = name
        self.year = year

    @classmethod
    def AddFilm(cls):
        return cls(name="Blade Runner", year="1982")

    @classmethod
    def RemoveFilm(cls):
        return cls(name="Gladiator", year="2000")