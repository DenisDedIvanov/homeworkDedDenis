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
    return ((a.get_1() - b.get_1()) ** 2 + (a.get_2() - b.get_2()) ** 2) ** 0.5

class Shape:
    def __init__(self, type = 'Shape'):
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
        return self._x1 + self._x2 + self._x3

    def area(self):
        pp = self.perimeter() / 2
        return (pp * (pp - self._x2) * (pp - self._x2) * (pp - self._x3)) ** 0.5

class circle(Shape):
    def __init__(self, o, r, type = "circle"):
        super().__init__(type)
        self._r = r
        self._o = o

    def area(self):
        return 3.14 * len(self._o, self._r) ** 2

    def perimeter(self):
        return 2 * 3.14 * len(self._o, self._r)
class quadrangle(Shape):
    def __init__(self, point1, point2, point3, point4, type = "quadrangle"):
        super().__init__(type)
        self._point1 = point1
        self._point2 = point2
        self._point3 = point3
        self._point4 = point4
        self._x1 = len(self._point1, self._point2)
        self._x2 = len(self._point2, self._point3)
        self._x3 = len(self._point3, self._point4)
        self._x4 = len(self._point1, self._point4)

    def perimeter(self):
        return self._x1 + self._x2 + self._x3 + self._x4

class rectangle(quadrangle):
    def __init__(self, point1, point2, point3, point4, type = "rectangle"):
        super().__init__(point1, point2, point3, point4, type)

    def area(self):
        return self._x1 * self._x2

class square(rectangle):
    def __init__(self, point1, point2, point3, point4, type = "square"):
        super().__init__(point1, point2, point3, point4, type)

class rhombus(quadrangle):
    def __init__(self, point1, point2, point3, point4, type = "rhombus"):
        super().__init__(point1, point2, point3, point4, type)

    def area(self):
        return 0.5 * len(self._point1, self._point3) * len(self._point2, self._point4)

a = circle(Point(0,0), Point(0,1))
b = square (Point(0,0), Point(0,5), Point(5,5), Point(5,0))
print(a)
print(b)