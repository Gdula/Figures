from figures import *
from gui import *


class App(object):
    def run(self):
        gui = Gui()
        root = Tk()
        label = Label(root, text="Figury")
        label.pack()

        gui.draw_buttons(root)

        # gui.canvas(root)
        root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
