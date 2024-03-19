# Lab01
# Amanda Wang
# Camila Flores Diaz

"""
 Pygame base template for opening a window
 Sample Python/Pygame Programs

"""
import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

pygame.init()

# Set the width and height of the screen [width, height]
size = (700, 500)
screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # Exercise 1a

w, h = pygame.display.get_surface().get_size()
size = (w, h)
screen = pygame.display.set_mode(size)

pygame.display.set_caption("My First Pygame Game")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Starting position of rectangle
# Rectangle 1
center = screen.get_rect().center  # Exercise 1b
rect_x, rect_y = center

# Starting position of rectangle
# Rectangle 2
rect2_x = 30
rect2_y = 30

# Starting position of rectangle
# Rectangle 3
rect3_x = 100
rect3_y = 100

# Speed of rectangle in X and Y axis
# Rectangle 1
speed_x = 5
speed_y = 5

# Rectangle 2
rect2_speed_x = 3
rect2_speed_y = 3

# Rectangle 3
rect3_speed_x = 1
rect3_speed_y = 1

# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    # --- Game logic should go here
    if rect_x < 0 or rect_x > size[0] - 50:
        speed_x *= -1
    if rect_y < 0 or rect_y > size[1] - 100:
        speed_y *= -1

    if rect2_x < 0 or rect2_x > size[0] - 10:
        rect2_speed_x *= -1
    if rect2_y < 0 or rect2_y > size[1] - 65:
        rect2_speed_y *= -1

    if rect3_x < 0 or rect3_x > size[0] - 100:
        rect3_speed_x *= -1
    if rect3_y < 0 or rect3_y > size[1] - 150:
        rect3_speed_y *= -1

    # --- Screen-clearing code goes here

    # Here, we clear the screen to white. Don't put other drawing commands
    # above this, or they will be erased with this command.

    # If you want a background image, replace this clear with blit'ing the
    # background image.
    screen.fill(BLACK)

    # --- Drawing code should go here

    pygame.draw.rect(screen, WHITE, [rect_x, rect_y, 50, 50])
    rect_x += speed_x
    rect_y += speed_y
    print("rect_x =", rect_x, "rect_y =", rect_y)

    pygame.draw.rect(screen, RED, [rect2_x, rect2_y, 10, 10])
    rect2_x += rect2_speed_x
    rect2_y += rect2_speed_y
    print("rect2_x =", rect2_x, "rect2_y =", rect2_y)

    pygame.draw.rect(screen, GREEN, [rect3_x, rect3_y, 100, 100])
    rect3_x += rect3_speed_x
    rect3_y += rect3_speed_y
    print("rect3_x =", rect3_x, "rect3_y =", rect3_y)

    # pygame.draw.circle(screen, RED, [200, 140], 30, 5)

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()