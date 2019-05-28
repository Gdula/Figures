from tkinter import *
from abc import ABC, abstractmethod
import math


class ConvexPolygon(ABC):
    @abstractmethod
    def __init__(self, fill_colour, outline_colour):
        super().__init__()
        self.fill_colour = fill_colour
        self.outline_colour = outline_colour

    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

    @abstractmethod
    def draw(self, canvas):
        pass


class Triangle(ConvexPolygon):
    def __init__(self, fill_colour, outline_colour, a, b, c):
        super().__init__(fill_colour, outline_colour)
        self.a = a
        self.b = b
        self.c = c

    def area(self):
        return math.sqrt((1/2 * self.perimeter()) *
                         ((1/2 * self.perimeter() - self.a) *
                          (1/2 * self.perimeter() - self.b) *
                          (1/2 * self.perimeter() - self.c)))

    def perimeter(self):
        return self.a + self.b + self.c

    def draw(self, canvas):
        # determine corner points of triangle with sides a, b, c
        A = (0, 0)
        B = (self.c, 0)
        hc = (2 * (self.a ** 2 * self.b ** 2 + self.b ** 2 * self.c ** 2 + self.c ** 2 * self.a ** 2) -
              (self.a ** 4 + self.b ** 4 + self.c ** 4)) ** 0.5 / (2. * self.c)
        dx = (self.b ** 2 - hc ** 2) ** 0.5
        if abs((self.c - dx) ** 2 + hc ** 2 - self.a ** 2) > 0.01: dx = -dx
        C = (dx, hc)

        # move away from topleft, scale up a bit, convert to int
        coords = [int((x + 1) * 75) for x in A + B + C]
        canvas.create_polygon(coords, fill=self.fill_colour, outline=self.outline_colour)


class ConvexQuadrilateral(ConvexPolygon):
    def __init__(self, fill_colour, outline_colour, a, b, c, d):
        super().__init__(fill_colour, outline_colour)
        self.fill_colour = fill_colour
        self.outline_colour = outline_colour
        self.a = a
        self.b = b
        self.c = c
        self.d = d

    def area(self):
        semiperimeter = self.perimeter() / 2

        return math.sqrt((semiperimeter - self.a) *
                         (semiperimeter - self.b) *
                         (semiperimeter - self.c) *
                         (semiperimeter - self.d))

    def perimeter(self):
        return self.a + self.b + self.c + self.d

    def draw(self, canvas):
        pass


class RegularPentagon(ConvexPolygon):
    def __init__(self, fill_colour, outline_colour, a):
        super().__init__(fill_colour, outline_colour)
        self.a = a

    def area(self):
        return (math.sqrt(5 * (5 + 2 *
                          (math.sqrt(5)))) * self.a * self.a) / 4

    def perimeter(self):
        return 5 * self.a

    def draw(self, canvas):
        pass


class RegularHexagon(ConvexPolygon):
    def __init__(self, fill_colour, outline_colour, a):
        super().__init__(fill_colour, outline_colour)
        self.a = a

    def area(self):
        return ((3 * math.sqrt(3) *
                 (self.a * self.a)) / 2);

    def perimeter(self):
        return self.a * 6

    def draw(self, canvas):
        pass


class RegularOctagon(ConvexPolygon):
    def __init__(self, fill_colour, outline_colour, a):
        super().__init__(fill_colour, outline_colour)
        self.a = a

    def area(self):
        return 2 * (1 + (math.sqrt(2))) * self.a * self.a

    def perimeter(self):
        return 8 * self.a

    def draw(self, canvas):
        pass


class IsoscelesTriangle(Triangle):
    def __init__(self, fill_colour, outline_colour, a, b):
        super().__init__(fill_colour, outline_colour, a, a, b)

    def area(self):
        return super(IsoscelesTriangle, self).area()

    def perimeter(self):
        return super(IsoscelesTriangle, self).perimeter()

    def draw(self, canvas):
        pass


class EquilateralTriangle(Triangle):
    def __init__(self, fill_colour, outline_colour, a):
        super().__init__(fill_colour, outline_colour, a, a, a)

    def area(self):
        return super(EquilateralTriangle, self).area()

    def perimeter(self):
        return super(EquilateralTriangle, self).perimeter()

    def draw(self, canvas):
        pass


class Parallelogram(ConvexQuadrilateral):
    def __init__(self, fill_colour, outline_colour, a, b, c, d):
        super().__init__(fill_colour, outline_colour, a, b, c, d)

    def area(self):
        return super(Parallelogram, self).area()

    def perimeter(self):
        return super(Parallelogram, self).perimeter()

    def draw(self, canvas):
        pass


class Kite(ConvexQuadrilateral):
    def __init__(self, fill_colour, outline_colour, a, b):
        super().__init__(fill_colour, outline_colour, a, a, b, b)

    def area(self):
        return super(Kite, self).area()

    def perimeter(self):
        return super(Kite, self).perimeter()

    def draw(self, canvas):
        pass


class Rhombus(ConvexQuadrilateral):
    def __init__(self, fill_colour, outline_colour, a):
        super().__init__(fill_colour, outline_colour, a, a, a, a)

    def area(self):
        return super(Rhombus, self).area()

    def perimeter(self):
        return super(Rhombus, self).perimeter()

    def draw(self, canvas):
        pass


class Square(ConvexQuadrilateral):
    def __init__(self, fill_colour, outline_colour, a):
        super().__init__(fill_colour, outline_colour, a, a, a, a)

    def area(self):
        return super(Square, self).area()

    def perimeter(self):
        return super(Square, self).perimeter()

    def draw(self, canvas):
        pass


s = Square(1, 2, 2)
print(s.area())

t = Triangle("green", "black", 2, 3, 4)

t2 = IsoscelesTriangle('A', 'A', 2, 3)

print(t2.area())
# draw using Tkinter
root = Tk()
canvas = Canvas(root, width=500, height=300)

t.draw(canvas)

canvas.pack()
root.mainloop()




