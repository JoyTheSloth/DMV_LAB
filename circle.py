import pygame

pygame.init()

width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Animated Circle")

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)

x, y = width // 2, height // 2
radius = 20
speed = 5

clock = pygame.time.Clock()

running = True
while running:
    clock.tick(60)  

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        x -= speed
    if keys[pygame.K_RIGHT]:
        x += speed
    if keys[pygame.K_UP]:
        y -= speed
    if keys[pygame.K_DOWN]:
        y += speed

    if x - radius < 0:
        x = radius
    if x + radius > width:
        x = width - radius
    if y - radius < 0:
        y = radius
    if y + radius > height:
        y = height - radius

    screen.fill(WHITE)
    pygame.draw.circle(screen, BLUE, (x, y), radius)

    pygame.display.update()

pygame.quit()