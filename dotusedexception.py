# Класс DotUsedException

from boardexception import BoardException


class DotUsedException(BoardException):
    def __str__(self):
        return "Вы уже стреляли в данную точку!"
