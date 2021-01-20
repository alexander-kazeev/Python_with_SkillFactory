class PetCustomer:
    def __init__(self, name="", balance=0):
        self.__name = name
        self.__balance = balance

    def get_name(self):
        return self.__name

    def get_balance(self):
        return self.__balance

    def set_name(self, name):
        self.__name = name

    def set_balance(self, balance):
        self.__balance = balance

    def change_balance(self, change):
        self.__balance += change

    def __str__(self):
        return f"Клиент {self.get_name()}. Баланс: {self.get_balance()} руб."
