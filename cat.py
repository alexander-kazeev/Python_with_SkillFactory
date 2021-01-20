class Cat:
    def __init__(self, name="", gender=None, age=0):
        self.__name = name
        self.__gender = gender
        self.__age = age

    def get_name(self):
        return self.__name

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def set_name(self, name):
        self.__name = name

    def set_gender(self, gender):
        self.__gender = gender

    def set_age(self, age):
        self.__age = age

    def __str__(self):
        return f"{self.get_name()} {self.get_gender()} {self.get_age()}"
