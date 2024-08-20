import pygame
import random
import math

# Initialize Pygame
pygame.init()

# Set up display
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Pac-Man")

# Colors
black = (0, 0, 0)
yellow = (255, 255, 0)
red = (255, 0, 0)
white = (255, 255, 255)
blue = (0, 0, 255)

# Set up game variables
pacman_size = 20
pacman_x = screen_width // 2
pacman_y = screen_height // 2
pacman_speed = 5
pacman_dir = "RIGHT"

ghost_size = 20
ghosts = [{"x": random.randint(0, screen_width - ghost_size), "y": random.randint(0, screen_height - ghost_size), "color": red}]

dot_size = 5
dots = [(random.randint(0, screen_width - dot_size), random.randint(0, screen_height - dot_size)) for _ in range(50)]

score = 0
font = pygame.font.Font(None, 36)

# Load sounds
pygame.mixer.init()
eat_sound = pygame.mixer.Sound("eat.wav")
game_over_sound = pygame.mixer.Sound("game_over.wav")

# Game loop
running = True
clock = pygame.time.Clock()

def draw_pacman(x, y, size, direction):
    if direction == "RIGHT":
        pygame.draw.arc(screen, yellow, (x, y, size, size), math.radians(30), math.radians(330), 0)
    elif direction == "LEFT":
        pygame.draw.arc(screen, yellow, (x, y, size, size), math.radians(210), math.radians(150), 0)
    elif direction == "UP":
        pygame.draw.arc(screen, yellow, (x, y, size, size), math.radians(120), math.radians(60), 0)
    elif direction == "DOWN":
        pygame.draw.arc(screen, yellow, (x, y, size, size), math.radians(300), math.radians(240), 0)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        pacman_x -= pacman_speed
        pacman_dir = "LEFT"
    if keys[pygame.K_RIGHT]:
        pacman_x += pacman_speed
        pacman_dir = "RIGHT"
    if keys[pygame.K_UP]:
        pacman_y -= pacman_speed
        pacman_dir = "UP"
    if keys[pygame.K_DOWN]:
        pacman_y += pacman_speed
        pacman_dir = "DOWN"

    # Wrap around screen
    pacman_x = pacman_x % screen_width
    pacman_y = pacman_y % screen_height

    # Ghost AI
    for ghost in ghosts:
        if ghost["x"] < pacman_x:
            ghost["x"] += random.randint(1, 3)
        if ghost["x"] > pacman_x:
            ghost["x"] -= random.randint(1, 3)
        if ghost["y"] < pacman_y:
            ghost["y"] += random.randint(1, 3)
        if ghost["y"] > pacman_y:
            ghost["y"] -= random.randint(1, 3)

    # Check collision with dots
    pacman_rect = pygame.Rect(pacman_x, pacman_y, pacman_size, pacman_size)
    for dot in dots[:]:
        dot_rect = pygame.Rect(dot[0], dot[1], dot_size, dot_size)
        if pacman_rect.colliderect(dot_rect):
            dots.remove(dot)
            score += 1
            eat_sound.play()

    # Check collision with ghosts
    for ghost in ghosts:
        ghost_rect = pygame.Rect(ghost["x"], ghost["y"], ghost_size, ghost_size)
        if pacman_rect.colliderect(ghost_rect):
            running = False
            game_over_sound.play()
            print("Game Over! Final Score:", score)

    # Draw everything
    screen.fill(black)
    draw_pacman(pacman_x, pacman_y, pacman_size, pacman_dir)
    for ghost in ghosts:
        pygame.draw.rect(screen, ghost["color"], (ghost["x"], ghost["y"], ghost_size, ghost_size))
    for dot in dots:
        pygame.draw.rect(screen, white, (dot[0], dot[1], dot_size, dot_size))

    score_text = font.render(f"Score: {score}", True, blue)
    screen.blit(score_text, (10, 10))

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
