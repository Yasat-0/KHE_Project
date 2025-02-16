import pygame
import random
from assets import squirrel_img, obstacle_img, floor_img

ScoretoBeat = 2
GameState = "start"

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

# Main game loop
running = True
clock = pygame.time.Clock()

#Start Page
start_button = pygame.Rect(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 100)
start = False

#make a dev function followed by an if statemet to check if the player hit start
def running_game():

    global squirrel_x, squirrel_y, squirrel_velocity_y, is_jumping, obstacle_x, obstacle_y, score, running
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
    obstacle_x -= OBSTACLE_SPEED
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
    screen.blit(floor_img, (0, 0))

    # Draw squirrel
    screen.blit(squirrel_img, (squirrel_x, squirrel_y))

    # Draw obstacle
    screen.blit(obstacle_img, (obstacle_x, obstacle_y))

    # Draw score
    score_text = font.render(f"Score: {score}", True, BLACK)
    screen.blit(score_text, (10, 10))


    def check_score():
        global running, start, GameState
        if score >= ScoretoBeat:
            GameState = "paused"
            while GameState == "paused":
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        GameState = "end"
                        running = False
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            GameState = "start"  # Reset to start screen


                screen.fill(WHITE)
                pause_text = font.render(f"Congratulations! You reached {ScoretoBeat} points!", True, BLACK)
                pause_rect = pause_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 - 50))
                screen.blit(pause_text, pause_rect)

                continue_text = font.render("Press Enter to continue", True, BLACK)
                continue_rect = continue_text.get_rect(center=(WIDTH // 2, HEIGHT // 2 + 50))
                screen.blit(continue_text, continue_rect)

    check_score()

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







while running:
    if GameState == "running":
        running_game()
    elif GameState == "start":
        startScreen()

    pygame.display.flip()
    clock.tick(60)



pygame.quit()