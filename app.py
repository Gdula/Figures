from figures import *
from gui import *


class App(object):

    def __init__(self):
        self.gui = Gui()

    def run(self):
        root = Tk()
        self.gui.menu(root)
        root.mainloop()


if __name__ == '__main__':
    app = App()
    app.run()
