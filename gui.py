from tkinter import *
from figures import *


class Gui(object):

    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500

    def canvas(self, root):
        canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)

        CENTER = Point(self.WIDTH // 2, self.HEIGHT // 2)

        # p = RegularPolygon(5, 400, *CENTER, "red", "blue")
        po = RegularOctagon(400, *CENTER, "red", "blue")
        #for point in p.points:
            #print(point.x, point.y)

        #po.draw(canvas)
        #t = IsoscelesTriangle("white", "black", 2, 1)
        #t.draw(canvas)
        #t2 = EquilateralTriangle(400, *CENTER, "red", "blue")
        #t2.draw(canvas)
        c = Parallelogram("red", "black", Point(20, 20), Point(300, 30), Point(400, 100), Point(50, 200))
        c.draw(canvas)
        canvas.pack()

    def draw_buttons(self, root):
        top_frame = Frame(root)
        top_frame.pack()
        bottom_frame = Frame(root)
        bottom_frame.pack(side=BOTTOM)

        button_1 = Button(top_frame, text="Trójkąt", fg="green")
        button_2 = Button(top_frame, text="Czworokąt", fg="green")
        button_3 = Button(top_frame, text="Wielokąt foremny", fg="green")
        button_4 = Button(top_frame, text="Pentagon", fg="green")
        button_5 = Button(top_frame, text="Hexagon", fg="green")
        button_6 = Button(top_frame, text="Oktagon", fg="green")
        button_7 = Button(top_frame, text="Trójkąt równoramienny", fg="green")
        button_8 = Button(top_frame, text="Trójkąt równoboczny", fg="green")
        button_9 = Button(top_frame, text="Równoległobok", fg="green")
        button_10 = Button(top_frame, text="Deltoid", fg="green")
        button_11 = Button(top_frame, text="Romb", fg="green")
        button_12 = Button(top_frame, text="Kwadrat", fg="green")

        button_1.pack()
        button_2.pack()
        button_3.pack()
        button_4.pack()
        button_5.pack()
        button_6.pack()
        button_7.pack()
        button_8.pack()
        button_9.pack()
        button_10.pack()
        button_11.pack()
        button_12.pack()


