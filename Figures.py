class rectangle:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def area(self):
        return self.a * self.b
class square:
    def __init__(self, a):
        self.a = a
    def areaS(self):
        return self.a ** 2
class circle:
    def __init__(self, a):
        self.a = a
    def areaC(self):
        return (self.a * 3.14)/2
p = rectangle(3,4)
i = square(5)
m = circle(15)
f = [p, i, m]
for h in f:
    if isinstance(h, square):
        print('Площадь квадрата =', h.areaS())
    elif isinstance(h, rectangle):
        print('Площадь прямоугольника =', h.area())
    elif isinstance(h, circle):
        print('Площадь круга =', h.areaC())