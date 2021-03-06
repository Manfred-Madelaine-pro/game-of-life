import time
import random
from collections import namedtuple


Point = namedtuple("Point", ["i", "j"])
ADJACENT_POS = [
    Point(0, 1),
    Point(1, 1),
    Point(1, 0),
    Point(0, -1),
    Point(-1, -1),
    Point(-1, 0),
    Point(-1, 1),
    Point(1, -1),
]

REQUIRED_CELLS_FOR_LIVING = (2, 3)
REQUIRED_CELLS_FOR_REPRODUCTION = 3

MAX_ITER = 10
REFRESH_RATE = 0.3


class GameOfLife:
    grid = []
    rows = 0
    cols = 0
    token = True

    hard_set = False

    def __str__(self):
        alive_char = "I"
        dead_char = "."

        txt = ""
        for row in self.grid:
            txt += "\n"
            for cell in row:
                txt += alive_char if cell else dead_char

        return "The Great Game of Life !" + txt

    def init(self, width, length):
        for r in range(width):
            row = [not self.token] * length
            self.grid += [row]

        self.set_size()

    def set_grid(self, grid, token):
        self.hard_set = True

        if isinstance(grid, str):
            grid = txt_to_list(grid)

        for line in grid:
            row = []
            for c in line:
                row += [c == token]
            self.grid += [row]

        self.set_size()

    def init_life(self):
        if not self.hard_set:
            self.grid = [
                [random.choice([0, 1]) == 1 for __ in range(self.cols)]
                for _ in range(self.rows)
            ]
        print(self)

    def start(self):
        self.is_livingful = True

    def update(self):
        self.next()

        if self.extinct():
            self.is_livingful = False

    # ---------- HANDLE SIZE -----------

    def set_size(self):
        self.rows = len(self.grid)

        row_sizes = [len(r) for r in self.grid]
        if len(set(row_sizes)) > 1:
            self._correct_size_mismatch(max(row_sizes))
        self.cols = len(self.grid[0])

    def _correct_size_mismatch(self, max_len):
        for row in self.grid:
            if len(row) < max_len:
                row += [False]
        print("Size mismatch resolved !")

    def widden(self, rows, cols):
        self.add_columns(cols)
        self.add_rows(rows)  # always after updating the columns

    def add_columns(self, new_cols):
        for r in self.grid:
            r += [not self.token] * new_cols
        self.cols += new_cols

    def add_rows(self, new_rows):
        row = [not self.token] * self.cols
        for _ in range(new_rows):
            self.grid += [row]

        self.rows += new_rows

    # ---------- CORE -----------

    def play(self, max_iter=MAX_ITER):
        for i in range(max_iter):
            self.next()
            print(self)
            time.sleep(REFRESH_RATE)
            if self.extinct():
                break

    def next(self):
        next_grid = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                neighbors = self.get_neighbors(i, j)
                next_state = self.predict_next_state(self.grid[i][j], neighbors)
                row += [next_state]
            next_grid += [row]

        self.grid = next_grid

    def get_neighbors(self, i, j):
        neighbors_pos = [
            Point(i + adjacent.i, j + adjacent.j) for adjacent in ADJACENT_POS
        ]
        filtered_neighbors_pos = [n for n in neighbors_pos if self.is_valid_neighbor(n)]
        neighbors = [self.grid[n.i][n.j] for n in filtered_neighbors_pos]
        return neighbors

    def is_valid_neighbor(self, neighbor):
        return (
            neighbor.i >= 0
            and neighbor.j >= 0
            and neighbor.i < self.rows
            and neighbor.j < self.cols
        )

    def predict_next_state(self, cell, neighbors):
        if cell:
            return neighbors.count(self.token) in REQUIRED_CELLS_FOR_LIVING
        else:
            return neighbors.count(self.token) == REQUIRED_CELLS_FOR_REPRODUCTION

    # ---------- UTILS -----------

    def extinct(self):
        for r in self.grid:
            if True in r:
                return False
        return True


def txt_to_list(txt):
    return txt.replace(" ", "").split("\n")[1:-1]


def play(model):
    gol = GameOfLife()
    gol.set_grid(model, "#")
    print(gol)
    gol.play()


def main():
    test = """
    .......
    .##.##.
    .#.#.#.
    .#...#.
    .#...#.
    """

    play(test)


if __name__ == "__main__":
    main()
