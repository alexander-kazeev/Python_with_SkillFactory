class Volunteer:
    def __init__(self, name, city, status):
        self.__name = name
        self.__city = city
        self.__status = status

    def get_name(self):
        return self.__name

    def get_city(self):
        return self.__city

    def get_status(self):
        return self.__status

    def set_name(self, name):
        self.__name = name

    def set_city(self, city):
        self.__city = city

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return f"{self.get_name()}, {self.get_city()}, статус '{self.get_status()}'"
