import math
import numbers
class complexnum:

    def __init__(self, a = 0, b = 0):
        self.set(a, b)

    def set(self, a, b):
        self.re = a
        self.im = b

    def get(self):
        return self.re , self.im

    def conv_alg_to_exp(self):
        self.r = math.sqrt((self.re ** 2 + self.im ** 2))
        self.phi = math.atan(self.re / self.im)
        if self.re < 0 and self.im > 0:
            self.phi = math.pi - self.phi
        elif self.re < 0 and self.im < 0:
            self.phi = math.pi + self.phi
        elif self.re > 0 and self.im < 0:
            self.phi = - self.phi
        else:
            self.phi = self.phi
        self.re, self.im = self.r, self.phi
        return

    def conv_exp_to_alg(self):
        self.re, self.im = self.re * math.cos(self.im), self.re * math.sin(self.im)
        return

    def __add__(self, other):
        if isinstance(other, numbers.Number):
            return self.re + other, self.im
        else:
            return self.re + other.re, self.im + other.im

    def __radd__(self, other):
        if isinstance(other, numbers.Number):
            return self.re + other, self.im
        return self.re + other.re, self.im + other.im

    def __sub__(self, other):
        if isinstance(other, numbers.Number):
            return self.re - other, self.im
        else:
            return self.re - other.re, self.im - other.im

    def __rsub__(self, other):
        if isinstance(other, numbers.Number):
            return other - self.re, self.im
        else:
            return other.re - self.re, other.im - self.im

    def __mul__(self, other):
        if isinstance(other, numbers.Number):
            return self.re * other, self.im * other
        else:
            return self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re

    def __rmul__(self, other):
        if isinstance(other, numbers.Number):
            return self.re * other, self.im * other
        else:
            return other.re * self.re - other.im * self.im, other.re * self.im + other.im * self.re

    def __floordiv__(self, other):
        if isinstance(other, numbers.Number):
            return (self.re / other, self.im / other)
        else:
            return (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2), (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im ** 2)

    def __rfloordiv__(self, other):
        if isinstance(other, numbers.Number):
            return (other / self.re, other / self.im)
        return (other.re * self.re + other.im * self.im) / (self.re ** 2 + self.im ** 2), (other.im * self.re - other.re * self.im) / (self.re ** 2 + self.im ** 2)

    def __getitem__(self, key):
        if key == 0:
            return self.re
        elif key == 1:
            return self.im

    def __setitem__(self, key, value):
        if key == 0:
            self.re = value
        elif key == 1:
            self.im = value

    def __eq__(self, other):
        if isinstance(other, numbers.Number):
            return (self.re == other and self.im == 0)
        else:
            return self.re == other.re and self.im == other.im

    def __abs__(self):
        return (self.re**2 + self.im**2)**0.5

print("Введите два комплексных числа в формате: x1 y1 x2 y2, где z1 = x1 + iy1, z2 = x2 + iy2 .")
try:
    arr = [float(t) for t in input().split()]
except ValueError:
    print("Пожалуйста, введите числа!")
else:
    try:
        A = complexnum(arr[0], arr[1])
        B = complexnum(arr[2], arr[3])
    except IndexError:
        print("Вы ввели менее 4 чисел. Пожалуйста, введите 4 числа!")

print('Введите операцию:')
operator = input()
if operator == '+':
    print (A + B)
elif operator == '-':
    print(A - B)
elif operator == '*':
    print(A * B)
elif operator == '/':
    try:
        print(A // B)
    except ZeroDivisionError:
        print('Деление на ноль! Пожалуйста, ведите другое комплексное число!')
elif operator == 'abs':
    print('Модуль первого числа:', abs(A))
    print('Модуль второго числа:', abs(B))
try:
    if operator not in ("+", "-", '/', '*', 'abs'):
        raise TypeError
except TypeError:
    print('Вы ввели операцию непредусмотренную в данной программе')