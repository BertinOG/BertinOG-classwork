import pygame
import random

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
screen_width = 500
screen_height = 500
screen = pygame.display.set_mode((700, 500))

font = pygame.font.Font(None,36)

# Define the text and ggg variables outside of the drawGrid() method
text = font.render("0", True, (0, 0, 0))
ggg = 0

def drawGrid():
    global text, ggg  # Use the global text and ggg variables

    # Increment the value of ggg by 1
    ggg += 1

    # Update the text variable with the new value of ggg
    text = font.render(str(ggg), True, (0, 0, 0))

    blockSize = 50  # Set the size of the grid block
    for x in range(0, screen_width, blockSize):
        for y in range(0, screen_height, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(screen, BLACK, rect, 1)
            screen.blit(text, (x, y))

snake = [(0,0), (0,1), (1,1), (1,2), (1,3)]

# head

x, y = snake[0]
rect = pygame.Rect(x*50, y*50, 50, 50)
pygame.draw.rect(screen, GREEN, rect)

# tail

for x, y in snake[1:]:
    rect = pygame.Rect(x*50, y*50, 50, 50)
    pygame.draw.rect(screen, RED, rect)

pygame.display.set_caption("Snakes and Ladders")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(WHITE)

    # --- Drawing code should go here
    drawGrid()
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()