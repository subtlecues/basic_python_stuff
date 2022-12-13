#    Доопрацюйте класс Point так, щоб в атрибути x та y обʼєктів цього класу можна було записати тільки обʼєкти класу
#    int або float
#     Доопрацюйте класс Line так, щоб в атрибути begin та end обʼєктів цього класу можна було записати тільки обʼєкти класу Point
#     Створіть класс Triangle (трикутник), який задається трьома точками (обʼєкти классу Point). Реалізуйте перевірку даних,
# аналогічно до класу Line. Визначет метод, що містить площу трикутника. Для обчислень можна використати формулу Герона
# (https://en.wikipedia.org/wiki/Heron%27s_formula )

from abc import ABC, abstractmethod
import math


class Point:
    x = None
    y = None

    def __init__(self, x, y):
        if isinstance(x, float | int):
            self.x = x
        if isinstance(y, float | int):
            self.y = y


class Figure(ABC):
    pass
    # @abstractmethod
    # def area(self):
    #     pass
    #
    # @abstractmethod
    # def length(self):
    #     pass


class Line(Figure):
    begin = None
    end = None

    def __init__(self, begin, end):
        # check if Point-class obj received
        if isinstance(begin, Point):
            self.begin = begin
        if isinstance(end, Point):
            self.end = end

    def length(self):
        result = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return result
    # area = length


class Triangle(Figure):
    def __init__(self, a, b, c):
        if isinstance(a, Point):
            self.a = a
        if isinstance(b, Point):
            self.b = b
        if isinstance(c, Point):
            self.c = c

    def area(self):
        ab_length = math.dist([self.a.x, self.a.y], [self.b.x, self.b.y])
        bc_length = math.dist([self.b.x, self.b.y], [self.c.x, self.c.y])
        ac_length = math.dist([self.a.x, self.a.y], [self.c.x, self.c.y])
        half_perimetr = (ab_length + bc_length + ac_length) / 2
        area = math.sqrt(half_perimetr * (half_perimetr - ab_length) * (half_perimetr - bc_length) * (half_perimetr - ac_length))
        return area


p1 = Point(0,  0)
p2 = Point(3,  4)
p3 = Point(10, 2)

my_triangle = Triangle(p1, p2, p3)

print(my_triangle.area())