from tkinter import *
from app import *
from figures import *


class Gui(object):

    def __init__(self):
        self.WIDTH = 500
        self.HEIGHT = 500
        self.CENTER = Point(self.WIDTH // 2, self.HEIGHT // 2)

    def canvas(self, root):
        canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)

        p = RegularPolygon(5, 400, *self.CENTER, "red", "blue")
        po = RegularOctagon(400, *self.CENTER, "red", "blue")

        #po.draw(canvas)
        #t = IsoscelesTriangle("white", "black", 2, 1)
        #t.draw(canvas)
        #t2 = EquilateralTriangle(400, *CENTER, "red", "blue")
        #t2.draw(canvas)
        #canvas.delete(All)
        c = Parallelogram("red", "black", Point(10, 20), Point(300, 30), Point(400, 100), Point(50, 200))
        c.draw(canvas)
        canvas.pack()

    def menu(self, root):
        root.destroy()
        root = Tk()
        #canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        enter_button = Button(root, text="Trójkąt", command=lambda: self.triangle_page(root))
        enter_button.pack()
        #canvas.pack()
        enter_button = Button(root, text="Wielokąt", command=lambda: self.convex_quadrilateral_page(root))
        enter_button.pack()

        enter_button = Button(root, text="Wielokąt foremny", command=lambda: self.regular_polygon_page(root))
        enter_button.pack()

        enter_button = Button(root, text="Hexagon", command=lambda: self.regular_hexagon_page(root))
        enter_button.pack()

    def triangle_page(self, root):
        root.destroy()
        root = Tk()
        canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        canvas.pack()
        top_frame = Frame(root)
        top_frame.pack()
        bottom_frame = Frame(root)
        bottom_frame.pack(side=BOTTOM)

        text = Label(root, text="Trójkąt")
        text.pack()

        fill_colour = StringVar()
        entry = Entry(root, width=10, textvariable=fill_colour)
        entry.pack()

        outline_colour = StringVar()
        entry = Entry(root, width=10, textvariable=outline_colour)
        entry.pack()

        a_label = IntVar()
        entry = Entry(root, width=10, textvariable=a_label)
        entry.pack()

        b_label = IntVar()
        entry = Entry(root, width=10, textvariable=b_label)
        entry.pack()

        c_label = IntVar()
        entry = Entry(root, width=10, textvariable=c_label)
        entry.pack()

        enter_button = Button(root, text="Enter",command=lambda: self.draw_triangle(fill_colour.get(),
                                                                                    outline_colour.get(), a_label.get(), b_label.get(), c_label.get(), canvas))
        enter_button.pack()

        enter_button = Button(root, text="Wróć do menu", command=lambda: self.menu(root))
        enter_button.pack()

    def convex_quadrilateral_page(self, root):
        root.destroy()
        root = Tk()
        canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        canvas.pack()
        text = Label(root, text="Czworokąt")
        text.pack()

        fill_colour = StringVar()
        entry = Entry(root, width=10, textvariable=fill_colour)
        entry.pack()

        outline_colour = StringVar()
        entry = Entry(root, width=10, textvariable=outline_colour)
        entry.pack()

        a_label_x = IntVar()
        entry = Entry(root, width=10, textvariable=a_label_x)
        entry.pack()

        a_label_y = IntVar()
        entry = Entry(root, width=10, textvariable=a_label_y)
        entry.pack()

        b_label_x = IntVar()
        entry = Entry(root, width=10, textvariable=b_label_x)
        entry.pack()

        b_label_y = IntVar()
        entry = Entry(root, width=10, textvariable=b_label_y)
        entry.pack()

        c_label_x = IntVar()
        entry = Entry(root, width=10, textvariable=c_label_x)
        entry.pack()

        c_label_y = IntVar()
        entry = Entry(root, width=10, textvariable=c_label_y)
        entry.pack()

        d_label_x = IntVar()
        entry = Entry(root, width=10, textvariable=d_label_x)
        entry.pack()

        d_label_y = IntVar()
        entry = Entry(root, width=10, textvariable=d_label_y)
        entry.pack()

        enter_button = Button(root, text="Enter", command=lambda: self.draw_convex_quadrilateral(fill_colour.get(),
                                                                                                 outline_colour.get(), Point(a_label_x.get(), a_label_y.get()), Point(b_label_x.get(), b_label_y.get()),
                                                                                                 Point(c_label_x.get(), c_label_y.get()), Point(d_label_x.get(), d_label_y.get()), canvas))
        enter_button.pack()

        enter_button = Button(root, text="Wróć do menu", command=lambda: self.menu(root))
        enter_button.pack()

    def regular_polygon_page(self, root):
        root.destroy()
        root = Tk()
        canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        canvas.pack()
        text = Label(root, text="Wielokąt foremny")
        text.pack()

        fill_colour = StringVar()
        entry = Entry(root, width=10, textvariable=fill_colour)
        entry.pack()

        outline_colour = StringVar()
        entry = Entry(root, width=10, textvariable=outline_colour)
        entry.pack()

        num_sides = IntVar()
        entry = Entry(root, width=10, textvariable=num_sides)
        entry.pack()

        a = IntVar()
        entry = Entry(root, width=10, textvariable=a)
        entry.pack()

        enter_button = Button(root, text="Enter", command=lambda: self.draw_regular_polygon(num_sides.get(),
                                                    a.get(), fill_colour.get(), outline_colour.get(), canvas))
        enter_button.pack()

        enter_button = Button(root, text="Wróć do menu", command=lambda: self.menu(root))
        enter_button.pack()

    def regular_hexagon_page(self, root):
        root.destroy()
        root = Tk()
        canvas = Canvas(root, width=self.WIDTH, height=self.HEIGHT)
        canvas.pack()
        text = Label(root, text="Wielokąt foremny")
        text.pack()

        fill_colour = StringVar()
        entry = Entry(root, width=10, textvariable=fill_colour)
        entry.pack()

        outline_colour = StringVar()
        entry = Entry(root, width=10, textvariable=outline_colour)
        entry.pack()

        a = IntVar()
        entry = Entry(root, width=10, textvariable=a)
        entry.pack()

        enter_button = Button(root, text="Enter",
                              command=lambda: self.draw_regular_hexagon(a.get(), fill_colour.get(),
                                                                        outline_colour.get(), canvas))
        enter_button.pack()

        enter_button = Button(root, text="Wróć do menu", command=lambda: self.menu(root))
        enter_button.pack()

    def draw_triangle(self, fill_colour, outline_colour, a_label, b_label, c_label, canvas):
        canvas.delete("all")
        triangle = Triangle(fill_colour, outline_colour, a_label, b_label, c_label)
        canvas.create_text(150, 10, text=("Obwód", triangle.perimeter()))
        canvas.create_text(150, 30, text=("Pole ", triangle.area()))
        triangle.draw(canvas)

    def draw_convex_quadrilateral(self, fill_colour, outline_colour, A, B, C, D, canvas):
        canvas.delete("all")
        convex_quarilateral = ConvexQuadrilateral(fill_colour, outline_colour, A, B, C, D)
        canvas.create_text(150, 10, text=("Obwód", convex_quarilateral.perimeter()))
        canvas.create_text(150, 30, text=("Pole ", convex_quarilateral.area()))
        convex_quarilateral.draw(canvas)

    def draw_regular_polygon(self, num_sides, a, fill_colour, outline_colour, canvas):
        canvas.delete("all")
        regular_polygon = RegularPolygon(num_sides, a, *self.CENTER, fill_colour, outline_colour)
        canvas.create_text(150, 10, text=("Obwód", regular_polygon.perimeter()))
        canvas.create_text(150, 30, text=("Pole ", regular_polygon.area()))
        regular_polygon.draw(canvas)

    def draw_regular_hexagon(self, a, fill_colour, outline_colour, canvas):
        canvas.delete("all")
        regular_hexagon = RegularHexagon(a, *self.CENTER, fill_colour, outline_colour)
        canvas.create_text(150, 10, text=("Obwód", regular_hexagon.perimeter()))
        canvas.create_text(150, 30, text=("Pole ", regular_hexagon.area()))
        regular_hexagon.draw(canvas)
