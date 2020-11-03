
# Model
# grid : update 
# print grid

# Core
# Update grid
# parse old and populate new state

# track only living cells

# Test place one cell and see it evolve
# Display module

# history
# save/import figures

class GameOfLife:
	grid  = []

	# next()

	def __str__(self):
		alive_char = 'O'
		dead_char = '-'

		txt = ''
		for row in self.grid:
			txt += '\n'
			for cell in row:
				txt += alive_char if cell else dead_char

		return "The Great Game of Life !" + txt

	def populate_grid(self, txt_grid, living_cell_char):
		print(txt_grid)
		for line in txt_grid:
			row = []
			for c in line:
				row += [c == living_cell_char]
			self.grid += [row]


def txt_to_list(txt):
	return txt.replace('\t', '').split('\n')[1:-1]

def main():
	test = """
	.......
	.......
	...#...
	.......
	.......
	"""
	
	test_list = txt_to_list(test)
	print(test_list)

	gol = GameOfLife()
	gol.populate_grid(test_list, "#")

	print(gol)

main()