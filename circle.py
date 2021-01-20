from math import pi


class Circle:
    def __init__(self, radius):
        self.__radius = radius

    def get_radius(self):
        return self.__radius

    def set_radius(self, radius):
        self.__radius = radius

    def get_area(self):
        return pi * (self.__radius ** 2)
