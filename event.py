class Event:
    def __init__(self, name):
        self.__name = name
        self.__guests = []

    def get_name(self):
        return self.__name

    def get_guests(self):
        return self.__guests

    def set_name(self, name):
        self.__name = name

    def add_guest(self, guest):
        self.__guests.append(guest)

    def __str__(self):
        result = f"Гости события '{self.get_name()}':"
        for guest in self.get_guests():
            result += f"\n{guest}"
        return result
