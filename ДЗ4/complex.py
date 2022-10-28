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
             (self.re / other, self.im / othe)
        else:
            return (self.re * other.re + self.im * other.im) / (other.re ** 2 + other.im ** 2), (self.im * other.re - self.re * other.im) / (other.re ** 2 + other.im ** 2)

    def __rfloordiv__(self, other):
        if isinstance(other, numbers.Number):
            return (other / self.re, other / self.im)
        return (other.re * self.re + other.im * self.im) / (self.re ** 2 + self.im ** 2), (other.b * self.a - other.a * self.b) / (self.a ** 2 + self.b ** 2)

z1 = complexnum(1, 2)
z2 = complexnum(2, 3)
print(z1+z2, '-сумма двух комплексных чисел')
print(z1+9, '-сумма комплексного и действительного числа')
print(z1-z2, '-разность двух комплексных чисел')
print(z1-9, '-разность комплексного и действительного числа')
print(z1*z2, '-произведение двух комплексных чисел')
print(z1*9, '-произведение комплексного и действительного числа')
print(z1//z2, '-деление двух комплексных чисел')
print(z1//9, '-деление комплексного и действительного числа')