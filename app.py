from figures import *
from gui import *


class App(object):

    def __init__(self):
        self.gui = Gui()

    def run(self):
        gui = Gui()
        root = Tk()
        label = Label(root, text="Figury")
        #label.pack()

        #gui.draw_buttons(root)
        gui.menu(root)
        choice = "triangle"
        #app.figure_factory(choice, root)

        # gui.canvas(root)
        root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
