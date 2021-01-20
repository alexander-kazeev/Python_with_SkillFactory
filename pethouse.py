from cat import Cat
from petcustomer import PetCustomer
from volunteer import Volunteer
from event import Event

print("\nЗадание 1.8.1.")
cat_baron = Cat(name="Барон", gender="Мальчик", age=2)
cat_sam = Cat(name="Сэм", gender="Мальчик", age=2)
print(cat_baron)
print(cat_sam)

print("\nЗадание 1.10.3.")
customer_petrov = PetCustomer(name="Иван Петров", balance=90)
customer_petrov.change_balance(-40)
print(customer_petrov)

print("\nЗадание 1.10.4.")
volunteer_petrov = Volunteer(name="Иван Петров", city="г. Москва", status="Наставник")
volunteer_ivanov = Volunteer(name="Илья Иванов", city="г. Ярославль", status="Стажер")
volunteer_sidorov = Volunteer(name="Семен Сидоров", city="г. Санкт-Петербург", status="Стажер")
volunteer_orlov = Volunteer(name="Олег Орлов", city="г. Орел", status="Наставник")
corporate = Event("Корпоратив для волонтеров")
corporate.add_guest(volunteer_petrov)
corporate.add_guest(volunteer_sidorov)
print(corporate)
