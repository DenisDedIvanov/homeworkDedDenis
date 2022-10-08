import math
class complexnum:

    def __init__(self, a = 0, b = 0):
        self.set(a, b)

    def set(self, a, b):
        self.re = a
        self.im = b

    def get(self):
        return self.re , self.im

def sum(self, other):
    return complexnum(self.re + other.re, self.im + other.im)
z1 = complexnum(1, 2)
z2 = complexnum(2, 3)
z = sum(z1, z2)
print(*z.get())










