import pygame
import os

# Initialize Pygame
pygame.init()

# Define the path to the Downloads directory
DOWNLOADS_DIR = os.path.join(os.path.expanduser('~'), 'Downloads')

# Load images
squirrel_img = pygame.image.load(os.path.join(DOWNLOADS_DIR, 'PixelSquirrelNoBackground.png.png'))
obstacle_img = pygame.image.load(os.path.join(DOWNLOADS_DIR, 'PixelTree.png'))
floor_img = pygame.image.load(os.path.join(DOWNLOADS_DIR, 'background.png'))

# Scale images to half their size
squirrel_img = pygame.transform.scale(squirrel_img, (squirrel_img.get_width() // 2.75, squirrel_img.get_height() // 2))
obstacle_img = pygame.transform.scale(obstacle_img, (obstacle_img.get_width() // 1.5, obstacle_img.get_height() // 1))

# Scale background to fit the screen
floor_img = pygame.transform.scale(floor_img, (1200, 600))
