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
pygame.display.set_caption("X-Y Plane Animation")

WHITE = (255, 255, 255)
BLUE = (0, 120, 255)
BLACK = (0, 0, 0)

# Origin at center
origin_x = WIDTH // 2
origin_y = HEIGHT // 2

# Circle position in Cartesian coordinates
x, y = 0, 0   # (0,0) at center

dx, dy = speed, speed

clock = pygame.time.Clock()

# Convert Cartesian → Screen coordinates
def to_screen(x, y):
    screen_x = origin_x + x
    screen_y = origin_y - y   # invert Y-axis
    return int(screen_x), int(screen_y)

# --- GAME LOOP ---
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Move in XY plane
    x += dx
    y += dy

    # Convert to screen position
    sx, sy = to_screen(x, y)

    # Bounce (based on screen boundaries)
    if sx - radius <= 0 or sx + radius >= WIDTH:
        dx = -dx
    if sy - radius <= 0 or sy + radius >= HEIGHT:
        dy = -dy

    # Draw
    screen.fill(WHITE)

    # Draw X and Y axes
    pygame.draw.line(screen, BLACK, (0, origin_y), (WIDTH, origin_y), 2)  # X-axis
    pygame.draw.line(screen, BLACK, (origin_x, 0), (origin_x, HEIGHT), 2)  # Y-axis

    # Draw circle
    pygame.draw.circle(screen, BLUE, (sx, sy), radius)

    pygame.display.flip()
    clock.tick(60)