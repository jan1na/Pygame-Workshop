import pygame
import sys

# Initialize pygame
pygame.init()

# --- Screen setup ---
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Starter Template")

# --- Clock (FPS) ---
FPS = 60
clock = pygame.time.Clock()

# --- Colors ---
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (200, 0, 0)
BLUE = (0, 100, 255)

# --- Fonts ---
font = pygame.font.SysFont(None, 36)

# --- Player setup ---
player = pygame.Rect(100, 100, 50, 50)
player_speed = 5

# --- Example obstacle ---
obstacle = pygame.Rect(400, 300, 100, 100)

# --- Score or timer ---
start_ticks = pygame.time.get_ticks()

# --- Game loop ---
running = True
while running:
    clock.tick(FPS)  # Limit FPS

    # --- Event handling ---
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # --- Input ---
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.x -= player_speed
    if keys[pygame.K_RIGHT]:
        player.x += player_speed
    if keys[pygame.K_UP]:
        player.y -= player_speed
    if keys[pygame.K_DOWN]:
        player.y += player_speed

    # --- Collision detection ---
    if player.colliderect(obstacle):
        print("Collision!")

    # --- Drawing ---
    screen.fill(WHITE)

    # Draw player and obstacle
    pygame.draw.rect(screen, BLUE, player)
    pygame.draw.rect(screen, RED, obstacle)

    # Draw timer
    seconds = (pygame.time.get_ticks() - start_ticks) / 1000
    timer_text = font.render(f"Time: {seconds:.2f}s", True, BLACK)
    screen.blit(timer_text, (10, 10))

    # --- Update display ---
    pygame.display.flip()

# --- Cleanup ---
pygame.quit()
sys.exit()
