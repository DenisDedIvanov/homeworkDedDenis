import math
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

def sum(self, other):
    return complexnum(self.re + other.re, self.im + other.im)
z1 = complexnum(1, 2)
z2 = complexnum(2, 3)
zsum = sum(z1, z2)
print(zsum.get(), '-сумма')

def sub(self, other):
    return complexnum(self.re - other.re, self.im - other.im)
zsub = sub(z1, z2)
print(zsub.get(), '-разность')

def mult(self, other):
    return complexnum((self.re * other.re) - (self.im * other.im), (self.im * other.re) + (self.re * other.im))
zmult = mult(z1, z2)
print(zmult.get(), '-произведение')

def div(self, other):
    r = (other.re ** 2 + other.im ** 2)
    return complexnum((self.re * other.re + self.im * other.im) / r, (self.im * other.re - self.re * other.im) / r)
zdiv = div(z1, z2)
print(zdiv.get(), '-частное')

za = complexnum(1, 1)
za.conv_alg_to_exp()
print(za.get(), "-конвертация из алгебраической в показательную форму")
za.conv_exp_to_alg()
print(za.get(), "-конвертация из показательной в алгебраическую форму")
