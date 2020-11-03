# Model
# grid : update
# [x] print grid

# Core
# Update grid
# parse old and populate new state

# track only living cells

# Test place one cell and see it evolve
# Display module

# history
# save/import figures


class GameOfLife:
    grid = []
    rows = 0
    cols = 0

    def __str__(self):
        alive_char = "O"
        dead_char = "-"

        txt = ""
        for row in self.grid:
            txt += "\n"
            for cell in row:
                txt += alive_char if cell else dead_char

        return "The Great Game of Life !" + txt

    def populate_grid(self, txt_grid, alive_char):
        for line in txt_grid:
            row = []
            for c in line:
                row += [c == alive_char]
            self.grid += [row]

        self.set_size()

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

    def next(self):
        next_grid = []

        for i in range(self.rows):
            row = []
            for j in range(self.cols):
                neighbors = self.get_neighbors(i, j)
                next_state = self.predict_next_state(neighbors)
                row += [next_state]
            next_grid += [row]

        self.grid = next_grid

    def get_neighbors(self, i, j):
        pass

    def predict_next_state(self, neighbors):
        pass


def txt_to_list(txt):
    return txt.replace(" ", "").split("\n")[1:-1]


def main():
    test = """
    .......
    .......
    ...#...
    .......
    .......
    """

    test_list = txt_to_list(test)

    gol = GameOfLife()
    gol.populate_grid(test_list, "#")
    print(gol)

    # gol.next()


main()
