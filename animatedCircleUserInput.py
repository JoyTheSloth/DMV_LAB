import pygame
import sys

# --- USER INPUT ---
try:
    WIDTH = int(input("Enter window width (e.g. 800): "))
    HEIGHT = int(input("Enter window height (e.g. 600): "))
    radius = int(input("Enter circle radius (e.g. 20): "))
    speed = int(input("Enter speed (e.g. 5): "))
except:
    print("Invalid input! Using default values.")
    WIDTH, HEIGHT = 800, 600
    radius, speed = 20, 5

# --- INIT ---
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Positive X-Y Axes (Left to Right Motion)")

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

clock = pygame.time.Clock()

# Origin at bottom-left
origin_x = 0
origin_y = HEIGHT

# Circle position (Cartesian)
x = 0          # start at left
y = HEIGHT // 2  # fixed height (positive Y)

dx = speed     # only horizontal movement

# Convert Cartesian → Screen
def to_screen(x, y):
    screen_x = origin_x + x
    screen_y = origin_y - y
    return int(screen_x), int(screen_y)

# --- GAME LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move ONLY left → right
    x += dx

    # Bounce at boundaries (horizontal only)
    if x <= radius or x >= WIDTH - radius:
        dx = -dx

    # Convert position
    sx, sy = to_screen(x, y)

    # --- DRAW ---
    screen.fill(WHITE)

    # Draw axes (only positive axes)
    pygame.draw.line(screen, BLACK, (0, HEIGHT), (WIDTH, HEIGHT), 3)  # X-axis
    pygame.draw.line(screen, BLACK, (0, HEIGHT), (0, 0), 3)           # Y-axis

    # Draw circle
    pygame.draw.circle(screen, BLUE, (sx, sy), radius)

    pygame.display.flip()
    clock.tick(60)