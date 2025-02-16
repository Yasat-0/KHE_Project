import pygame
import random
from assets import squirrel_img, obstacle_img, floor_img, PullutionBackground, PollutionObstacle, PovertyCity, Dumpster

# Initialize Pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 1200, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Squirrels for Life")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 50, 0)
RED = (255, 0, 0)  # Color for the obstacle border

# Game settings
GRAVITY = 0.8
JUMP_STRENGTH = 23  # Increased jump strength
OBSTACLE_SPEED = 10

# Squirrel settings
squirrel_width = squirrel_img.get_width()
squirrel_height = squirrel_img.get_height()
squirrel_x = 50
squirrel_y = HEIGHT - squirrel_height - 40
squirrel_velocity_y = 0
is_jumping = False

# Obstacle settings
obstacle_width = obstacle_img.get_width()
obstacle_height = obstacle_img.get_height()
obstacle_x = WIDTH
obstacle_y = HEIGHT - obstacle_height - 20

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Levels
level = 1
ScoretoBeat = 5
GameState = "start"
current_Background = floor_img
current_Obstacle = obstacle_img

# Main game loop
running = True
clock = pygame.time.Clock()

# Start Page
start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
start = False

def running_game():
    global squirrel_x, squirrel_y, squirrel_velocity_y, is_jumping, obstacle_x, obstacle_y, score, running, GameState, current_Background, current_Obstacle

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not is_jumping:
                is_jumping = True
                squirrel_velocity_y = -JUMP_STRENGTH

    # Apply gravity
    if is_jumping:
        squirrel_velocity_y += GRAVITY
        squirrel_y += squirrel_velocity_y
        if squirrel_y >= HEIGHT - squirrel_height - 10:
            squirrel_y = HEIGHT - squirrel_height - 10
            is_jumping = False
            squirrel_velocity_y = 0

    # Move obstacle
    obstacle_x -= OBSTACLE_SPEED + (score + level * 5) / 2
    if obstacle_x < -obstacle_width:
        obstacle_x = WIDTH
        obstacle_y = HEIGHT - obstacle_height - 10
        score += 1  # Increment score when the obstacle is passed

    # Check for collision
    squirrel_rect = pygame.Rect(squirrel_x, squirrel_y, squirrel_width, squirrel_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if squirrel_rect.colliderect(obstacle_rect):
        # Restart the game
        squirrel_y = HEIGHT - squirrel_height - 10
        squirrel_velocity_y = 0
        is_jumping = False
        obstacle_x = WIDTH
        score = 0  # Reset score on collision

    # Clear the screen
    screen.fill(WHITE)

    # Draw floor
    screen.blit(current_Background, (0, 0))

    # Draw squirrel
    screen.blit(squirrel_img, (squirrel_x, squirrel_y))

    # Draw obstacle
    screen.blit(current_Obstacle, (obstacle_x, obstacle_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))

    check_score()

def check_score():
    global running, GameState, current_Background, current_Obstacle, level, ScoretoBeat
    if score >= ScoretoBeat:
        if level == 1:
            level += 1
            ScoretoBeat = ScoretoBeat + 5
            current_Background = PullutionBackground 
            current_Obstacle = PollutionObstacle
            GameState = "break"
        elif level == 2:
            level += 1
            ScoretoBeat = ScoretoBeat + 5
            current_Background = PovertyCity
            current_Obstacle = Dumpster
            GameState = "break"
        else:
            GameState = "win"

def startScreen():
    global running, start, GameState
    screen.blit(floor_img, (0, 0))
    
    # Display the introductory text
    intro_text = font.render("Join the squirrel's journey through a changing environment!", True, BLACK)
    intro_rect = intro_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 100))
    screen.blit(intro_text, intro_rect)
    
    pygame.draw.rect(screen, GREEN, start_button)
    start_text = font.render("Start", True, WHITE)
    text_rect = start_text.get_rect(center=start_button.center)
    screen.blit(start_text, text_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_button.collidepoint(event.pos):
                GameState = "running"

def breakScreen():
    global running, GameState, current_Background, current_Obstacle
    screen.blit(current_Background, (0, 0))

    break_text = font.render(f"Congratulations! You reached {ScoretoBeat} points!", True, BLACK)
    break_rect = break_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
    screen.blit(break_text, break_rect)
    
    continue_text = font.render("Travel to the next area", True, BLACK)
    continue_rect = continue_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
    screen.blit(continue_text, continue_rect)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                GameState = "running"
                reset_game()

def reset_game():
    global squirrel_y, squirrel_velocity_y, is_jumping, obstacle_x, score
    squirrel_y = HEIGHT - squirrel_height - 10
    squirrel_velocity_y = 0
    is_jumping = False
    obstacle_x = WIDTH
    score = 0

while running:
    if GameState == "running":
        running_game()
    elif GameState == "start":
        startScreen()
    elif GameState == "break":
        breakScreen()
    elif GameState == "win":
        screen.fill(WHITE)
        win_text = font.render("You made it through to the end! However, the affects of everything you went through has caused so much harm to your body that you ", True, BLACK)
        win_rect = win_text.get_rect(center=(WIDTH // 2, HEIGHT // 2))
        screen.blit(win_text, win_rect)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    pygame.display.flip()
    clock.tick(60)

pygame.quit()