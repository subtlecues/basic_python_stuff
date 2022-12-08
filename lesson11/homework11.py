#Створіть клас "Транспортний засіб" та підкласи "Автомобіль", "Літак", "Корабель", наслідувані від "Транспортний засіб".
# Наповніть класи атрибутами на свій розсуд. Створіть обʼєкти класів "Автомобіль", "Літак", "Корабель".


class Vehicle:
    fuel = None
    wheels = None
    windows = None
    environment = None


class ECar(Vehicle):
    fuel = 'electric'
    wheels = 4
    windows = 6
    environment = 'road'


class Plane(Vehicle):
    fuel = 'gasoline'
    wheels = 4
    windows = 14
    environment = 'air'


class Ship(Vehicle):
    fuel = 'heavy fuel oil'
    wheels = None
    windows = 50
    environment = 'water'


nissan_leaf = ECar()
boeing747 = Plane()
titanic = Ship()

# print(type(nissan_leaf))
# print(type(boeing747))
# print(type(titanic))