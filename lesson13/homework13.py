#     Доопрацюйте всі реревірки на типи даних (x, y в Point, begin, end в Line, etc) - зробіть перевірки за допомогою
#     property або класса-дескриптора.
#     Доопрацюйте класс Triangle з попередньої домашки наступним чином:
#     обʼєкти классу Triangle можна порівнювати між собою (==, !=, >, >=, <, <=) за площею.
#     перетворення обʼєкту классу Triangle на стрінг показує координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3

from abc import ABC, abstractmethod
import math


class Point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        if not isinstance(x, float | int):
            raise TypeError('Invalid value for point coordinates. Use int/float instead')
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        if not isinstance(y, float | int):
            raise TypeError('Invalid value for point coordinates. Use int/float instead')
        self._y = y


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

    def __init__(self, begin, end):
        self.begin = begin
        self.end = end

    @property
    def begin(self):
        return self._begin

    @begin.setter
    def begin(self, begin):
        if not isinstance(begin, Point):
            raise TypeError('Not point object received.')
        self._begin = begin

    @property
    def end(self):
        return self._end

    @end.setter
    def end(self, end):
        if not isinstance(end, Point):
            raise TypeError('Not point object received.')
        self._end = end

    def length(self):
        result = ((self.begin.x - self.end.x) ** 2 + (self.begin.y - self.end.y) ** 2) ** 0.5
        return result
    # area = length


class Triangle(Figure):
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    @property
    def a(self):
        return self._a

    @a.setter
    def a(self, a):
        if not isinstance(a, Point):
            raise TypeError('Not point object received.')
        self._a = a

    @property
    def b(self):
        return self._b

    @b.setter
    def b(self, b):
        if not isinstance(b, Point):
            raise TypeError('Not point object received.')
        self._b = b

    @property
    def c(self):
        return self._c

    @c.setter
    def c(self, c):
        if not isinstance(c, Point):
            raise TypeError('Not point object received.')
        self._c = c

    def area(self):
        ab_length = math.dist([self.a.x, self.a.y], [self.b.x, self.b.y])
        bc_length = math.dist([self.b.x, self.b.y], [self.c.x, self.c.y])
        ac_length = math.dist([self.a.x, self.a.y], [self.c.x, self.c.y])
        half_perimetr = (ab_length + bc_length + ac_length) / 2
        area = math.sqrt(half_perimetr * (half_perimetr - ab_length) * (half_perimetr - bc_length) * (half_perimetr - ac_length))
        return area

    def __eq__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Cannot be compared with other than Triangle class')
        return self.area() == other.area()

    def __ne__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Cannot be compared with other than Triangle class')
        return self.area() != other.area()

    def __gt__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Cannot be compared with other than Triangle class')
        return self.area() > other.area()

    def __ge__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Cannot be compared with other than Triangle class')
        return self.area() >= other.area()

    def __lt__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Cannot be compared with other than Triangle class')
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Triangle):
            raise TypeError('Cannot be compared with other than Triangle class')
        return self.area() <= other.area()

    def __str__(self):
        """координати його вершин у форматі x1, y1 -- x2, y2 -- x3, y3"""
        return f'Triangle peaks are: {self.a.x},{self.a.y} -- {self.b.x},{self.b.y} -- {self.c.x},{self.c.y}'


p1 = Point(0,  0)
p2 = Point(3,  4)
p3 = Point(10, 2)
p4 = Point(0,  1)
p5 = Point(3,  4)
p6 = Point(10, 2)
my_triangle = Triangle(p1, p2, p3)
tri2 = Triangle(p4, p5, p6)
tri3 = Triangle(p1,p2,p3)

abc = '123'

# print(my_triangle == tri2)
# print(tri2 == my_triangle)
# print(tri3 == my_triangle)
# print(my_triangle != tri2)
# print(tri2 != my_triangle)
# print(tri2 < my_triangle)
# print(tri2 > my_triangle)
# print(tri3 > tri2)
# print(tri2 > my_triangle)
# print(tri2 <= my_triangle)
# print(tri2 <= my_triangle)
# print(my_triangle)