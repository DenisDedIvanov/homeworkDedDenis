class Point:
    def __init__(self, x=0, y=0):
        self._x = x
        self._y = y

    def get_1(self):
        return self._x

    def get_2(self):
        return self._y

    def set_1(self, x):
        self._x = x

    def set_2(self, y):
        self._y = y

def len(a,b):
    return ((a.get_x() - b.get_x()) ** 2 + (a.get_y() - b.get_y()) ** 2) ** 0.5

class Shape:
    def __init__(self, type = '0'):
        self._type = type

    def __str__(self):
        return ('Тип фигуры: ' + str(self._type) + ", S = " + str(self.area()) + ", P = " + str(self.perimeter()) + '.')

class triangle(Shape):
    def __init__(self, point1 ,point2 ,point3, type="triangle"):
        super().__init__(type)
        self._point1 = point1
        self._point2 = point2
        self._x1 = len(self._point1, self._point2)
        self._point3 = point3
        self._x2 = len(self._point2, self._point3)
        self._x3 = len(self._point1, self._point3)

    def perimeter(self):
        return (self._x1 + self._x2 + self._x3)

    def area(self):
        pp = self.perimeter() / 2
        return ((pp * (pp - self._x2) * (pp - self._x2) * (pp - self._x3)) ** 0.5)

class circle(Shape):
    def __init__(self, o, r, type = "circle"):
        super().__init__(type)
        self._r = r
        self._o = o

    def area(self):
        return round(3.14 * len(self._o, self._r) ** 2, 2)

    def perimeter(self):
        return round( 2 * 3.14 * len(self._o, self._r), 2)
