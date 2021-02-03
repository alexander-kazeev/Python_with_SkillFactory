# Класс BoardOutException

from boardexception import BoardException


class BoardOutException(BoardException):
    def __str__(self):
        return "Вы пытаетесь выстрелить за пределы игрового поля!"
