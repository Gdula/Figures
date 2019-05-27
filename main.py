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
    def draw(self):
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

    def draw(self):
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

        def draw(self):
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

        def draw(self):
            pass




t = Triangle("green", "black", 2, 3, 4)


# draw using Tkinter
root = Tk()
canvas = Canvas(root, width=500, height=300)

t.draw()

canvas.pack()
root.mainloop()




