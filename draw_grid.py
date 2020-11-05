import pygame   # Provides what we need to make a game
import random   # Can generate random numbers

# Define dimensions of grid
DISPLAY_WIDTH = 640
DISPLAY_HEIGHT = 480
HALF_DISPLAY_WIDTH = DISPLAY_WIDTH / 2
HALF_DISPLAY_HEIGHT = DISPLAY_HEIGHT / 2
displaySize = (DISPLAY_WIDTH, DISPLAY_HEIGHT)

# Define size and number of cells
SIZE = 16
XCELLS = int(DISPLAY_WIDTH/SIZE)
YCELLS = int(DISPLAY_HEIGHT/SIZE)

# Create a list of colours
colours = []
colours.append((255, 255, 255))
colours.append((  0,   0,   0))
WHITE = 0
BLACK = 1

# Constants for Left and Right Mouse button events
LEFT = 1
RIGHT = 3

# Create a list for cells in the grid
grid = [[WHITE for y in range(YCELLS)] for x in range(XCELLS)]

# Define a function to initialise all the cells
def initGrid(grid, c):
    for y in range(YCELLS):
        for x in range(XCELLS):
            grid[x][y] = c
        
# Define a function to draw a square of colour(c) at coordinates, x and y
def drawCell(x, y, c):
    pygame.draw.rect(screen, colours[c], pygame.Rect(x * SIZE, y * SIZE, SIZE-1, SIZE-1))

# Define a function to update cells on screen from grid
def update():
    for y in range(YCELLS):
        for x in range(XCELLS):
            c = grid[x][y]
            drawCell(x, y, c)
               
# Initialise pygame
pygame.init()

# Set the window title
pygame.display.set_caption("Draw a grid of cells")

# Create the window
screen = pygame.display.set_mode(displaySize)

# Blank screen
screen.fill(BLACK)

# Initialise the generations
initGrid(grid, WHITE)

# Update the full display surface to the screen
pygame.display.flip()
      
# Create a clock to manage time
clock = pygame.time.Clock()

# Initialise variables
done = False
drawingON = False
drawColour = WHITE

# Runs the game loop
while not done:
    # The code here runs when every frame is drawn
    # Get any events that have occurred, like close button(X) clicked
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
            
        # handle Mouse
        if event.type == pygame.MOUSEBUTTONDOWN:
            drawingON = True
            if event.button == LEFT:
                drawColour = BLACK
            elif event.button == RIGHT:
                drawColour = WHITE

        if event.type == pygame.MOUSEBUTTONUP:
            drawingON = False

        # Check for q key
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_q:
                done = True

    # Check for drawingON
    if drawingON:
        pos = pygame.mouse.get_pos()
        x = int(pos[0] / SIZE)
        y = int(pos[1] / SIZE)
        grid[x][y] = drawColour

    # Update and draw 
    update()

    # Update the full display surface to the screen
    pygame.display.flip()

    # Limit the game to 30 frames per second
    clock.tick(60)

print('Quitting')
pygame.quit()
