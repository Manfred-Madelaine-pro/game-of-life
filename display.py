from tkinter import *
from game_of_life import GameOfLife as gol


window_size = 1200
token = 0
block = [
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],  #
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],
    [1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0],  #
]


block_len = len(block[0])  #!!!
block_size = block_len * 6 if block_len <= 10 else window_size / block_len  # !!!


def add_button(fen):
    boutton_quit = Button(fen, text="Quit", command=fen.destroy)
    boutton_quit.grid(row=1, column=1, sticky=W + E, padx=3, pady=3)


def add_canevas(fen):
    canevas = Canvas(
        fen,
        width=block_len * block_size + 2,
        height=block_len * block_size + 2,
        bg="white",
    )
    canevas.grid(row=0, column=0, columnspan=2, padx=3, pady=3)
    return canevas


def add_grid(canevas):
    for line in range(block_len):
        transit = []
        for colonne in range(block_len):
            transit.append(
                canevas.create_rectangle(
                    colonne * block_size + 2,
                    line * block_size + 2,
                    (colonne + 1) * block_size + 2,
                    (line + 1) * block_size + 2,
                )
            )


def color_grid(canevas):
    r = 0
    for line in block:
        for value in line:
            r += 1
            if value == token:
                canevas.itemconfigure(r, outline="black", fill="black")
            else:
                canevas.itemconfigure(r, outline="black")


# -------------- Main --------------


def main():
    fen = Tk()
    fen.title("Damier")
    add_button(fen)
    canevas = add_canevas(fen)

    add_grid(canevas)
    color_grid(canevas)
    fen.mainloop()


main()
