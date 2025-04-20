import pygame
import random

# Init
pygame.init()
WIDTH, HEIGHT = 600, 1000
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Flappy Bird")
clock = pygame.time.Clock()

# Settings
gravity = 3
up_speed = 15
down_speed = 15
speed = 3
image_swapping = 4

# Bird
bird_images = [pygame.image.load(f"./flappy_bird_images/bird_{i}.png").convert_alpha() for i in range(1, 5)]
bird = bird_images[0].get_rect(center=(300, 500))
image_counter = 0
move_up_counter = 0
move_down_counter = 0

# Obstacles
obstacles = [pygame.Rect(200, 0, 100, 400), pygame.Rect(500, 500, 100, 600)]

# Timer
font = pygame.font.SysFont(None, 32)
start_time = pygame.time.get_ticks()

# Game loop
running = True
while running:
    clock.tick(60)
    screen.fill((140, 240, 240))

    # Events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                move_up_counter = 6
                move_down_counter = 0
            elif event.key == pygame.K_s:
                move_down_counter = 6
                move_up_counter = 0

    # Bird movement
    if move_up_counter > 0:
        bird.y -= up_speed
        move_up_counter -= 1
    elif move_down_counter > 0:
        bird.y += down_speed
        move_down_counter -= 1
    else:
        bird.y += gravity

    # Obstacle movement
    for obstacle in obstacles:
        obstacle.x -= speed

    # Draw bird and obstacles
    screen.blit(bird_images[image_counter // image_swapping], bird)
    for obstacle in obstacles:
        pygame.draw.rect(screen, (0, 100, 0), obstacle)

    # Collision
    if bird.bottom >= HEIGHT:
        running = False

    # Check for collisions with obstacles
    for obstacle in obstacles.copy():
        if bird.colliderect(obstacle):
            running = False
        # Remove obstacles that are out of the window
        if obstacle.right < 0:
            obstacles.remove(obstacle)
        # if the last obstacle is far enough from the right side of the screen, add a new one
        elif WIDTH - obstacles[-1].right >= random.randint(200, 400):
            top = random.choice([True, False])
            height = random.randint(400, 600)
            y = 0 if top else HEIGHT - height
            obstacles.append(pygame.Rect(WIDTH, y, 100, height))

    # Game difficulty scaling
    speed *= 1.0005
    gravity *= 1.0005
    up_speed *= 1.0005
    down_speed *= 1.0005

    # Image swapping to create animation
    image_counter = (image_counter + 1) % (len(bird_images) * image_swapping)

    # Timer text
    elapsed = pygame.time.get_ticks() - start_time
    text = font.render(f"Time: {elapsed / 1000:.2f}s", True, (0, 0, 0))
    screen.blit(text, (10, 10))

    # Update screen
    pygame.display.flip()

pygame.quit()
