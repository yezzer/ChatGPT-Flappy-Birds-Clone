# Flappy Birds clone

import pygame

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Define some constants
GRAVITY = 0.25
FLAP_STRENGTH = 5

class Obstacle:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height

    def update(self):
        # Move the obstacle from right to left
        self.x -= 1

    def draw(self, screen):
        # Draw the obstacle on the screen using the light red color
        pygame.draw.rect(screen, (255, 153, 153), [self.x, self.y, self.width, self.height])


class Bird:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.velocity = 0

    def update(self):
        self.velocity += GRAVITY
        self.y += self.velocity

    def flap(self):
        self.velocity = -FLAP_STRENGTH


pygame.init()

# Set the width and height of the screen [width,height]
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Flappy Birds")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Create the bird
bird = Bird(100, 100)

# Create a list of obstacles
obstacles = [
    Obstacle(500, 0, 50, 100),
    Obstacle(500, 600, 50, 100),
    Obstacle(700, 300, 50, 100),
    Obstacle(900, 100, 50, 100),
]

# Create a font object
font = pygame.font.Font(None, 72)
# -------- Main Program Loop -----------
while not done:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                bird.flap()

    # Update the bird
    bird.update()

    # Update the obstacles
    for obstacle in obstacles:
        obstacle.update()

    # Check if the bird hit an obstacle
    for obstacle in obstacles:
        if bird.x + 10 >= obstacle.x and bird.x - 10 <= obstacle.x + obstacle.width:
            if bird.y + 10 >= obstacle.y and bird.y - 10 <= obstacle.y + obstacle.height:
                # The bird hit an obstacle. Stop the game and display "GAME OVER"
                done = True

    # Draw the screen
    screen.fill(WHITE)

    # Draw the bird
    pygame.draw.circle(screen, BLACK, (int(bird.x), int(bird.y)), 10)

    # Draw the obstacles
    for obstacle in obstacles:
        obstacle.draw(screen)

    # If the game is over, display "GAME OVER" in big letters
    if done:
        text = font.render("GAME OVER", True, BLACK)
        screen.blit(text, [150, 300])

    # Update the screen
    pygame.display.flip()

    # Limit frames per second
    clock.tick(60)

# Close the window and quit.
pygame.quit()
