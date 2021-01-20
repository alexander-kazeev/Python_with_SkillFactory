class Rectangle:
    def __init__(self, x, y, width, height):
        self.__x = x
        self.__y = y
        self.__width = width
        self.__height = height

    def get_x(self):
        return self.__x

    def get_y(self):
        return self.__y

    def get_width(self):
        return self.__width

    def get_height(self):
        return self.__height

    def set_x(self, x):
        self.__x = x

    def set_y(self, y):
        self.__y = y

    def set_width(self, width):
        self.__width = width

    def set_height(self, height):
        self.__height = height

    def get_area(self):
        return self.__width * self.__height

    def __str__(self):
        return str(f"Rectangle ({self.get_x()}, {self.get_y()}, {self.get_width()}, {self.get_height()})")
