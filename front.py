import random
from tkinter import *

from game_of_life import GameOfLife

try:
    import generic_screen as screen
    import colors
except ImportError:
    from front import generic_screen as screen
    from front import colors


TITLE = "Game Of Life"


class Front(screen.GenericScreen):
    def __init__(self, back_model, width, length, conf={}):
        self.margin = conf["margin"] if conf else 2
        if conf:
            screen_conf = conf["screen"].values()
            super().__init__(width, length, *screen_conf)
        else:
            super().__init__(width, length)
        self.f.title(TITLE)
        self.back_model = back_model

        self.being_size = self.cell_size
        self.being_step = self.being_size

        self.init_entities()
        super().create_access_buttons()
        super().bind_shortcuts()

        self.f.mainloop()

    def init_entities(self):
        self.front_cells = {}
        for i in range(self.width):
            for j in range(self.length):
                x0 = i * self.cell_size + self.margin
                y0 = j * self.cell_size + self.margin
                x1 = self.cell_size * self.width - self.margin
                y1 = self.cell_size * self.width - self.margin
                rect_id = self.canvas.create_rectangle(x0, y0, x1, y1, fill="white")

                self.canvas.itemconfig(rect_id, tags=(str(i + 1), str(j + 1)))
                self.front_cells[(i, j)] = rect_id

    # ------------------------- Overrided Methods --------------------------------

    def init_world(self):
        self.back_model.init_life()

    def update(self):
        self.back_model.update()
        self.draw_cells()

    # ---------------------------------------------------------

    def draw_cells(self):
        for i in range(self.width):
            for j in range(self.length):
                alive = self.back_model.grid[i][j]
                if alive:
                    c = self.pick_color(i, j)
                    self.change_color(i, j, c, rand=True)
                else:
                    self.change_color(i, j, colors.WHITE)

    def change_color(self, row, column, color_hue, rand=False):
        if rand:
            color_hex = colors.get_color_with_random_lightness(color_hue)
        else:
            color_hex = colors.get_hex(color_hue)
        self.canvas.itemconfig(self.front_cells[(row, column)], fill=color_hex)

    def pick_color(self, i, j):
        all_colors = [colors.BLUE, colors.GREEN, colors.RED, colors.PURPLE]
        m = min(i, j)
        color_zone = self.back_model.cols / len(all_colors)
        ind = int(m / color_zone)

        return all_colors[ind]


# ---------------------------------------------------------


def headless_man():
    model = """
    ---------
    --OO-----
    --O---O--
    ---OOOO--
    ---------
    ---OOOO--
    --O---O--
    --OO-----
    ---------
    """

    gol = GameOfLife()
    gol.set_grid(model, "O")
    print(gol)
    front = Front(gol, gol.rows, gol.cols)


def random_try(size):
    width = size
    length = width

    gol = GameOfLife()
    gol.init(width, length)
    print(gol)
    front = Front(gol, width, length)


if __name__ == "__main__":
    random_try(33)
    # headless_man()
