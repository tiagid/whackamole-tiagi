'''
Daniel Tiagi - Lab 10 - 10/18/24
'''


import pygame
import random

# Constants
SCREEN_WIDTH = 640  # 20 columns * 32 pixels
SCREEN_HEIGHT = 512  # 16 rows * 32 pixels
GRID_SIZE = 32  # Size of each square in the grid
BACKGROUND_COLOR = "light green"
GRID_COLOR = "black"

def draw_grid(screen):
    """Draw a 20x16 grid of 32x32 squares."""
    for x in range(0, SCREEN_WIDTH, GRID_SIZE):  # Vertical lines
        pygame.draw.line(screen, GRID_COLOR, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, GRID_SIZE):  # Horizontal lines
        pygame.draw.line(screen, GRID_COLOR, (0, y), (SCREEN_WIDTH, y))

def move_mole():
    """Get a random position for the mole."""
    x = random.randrange(0, SCREEN_WIDTH, GRID_SIZE)
    y = random.randrange(0, SCREEN_HEIGHT, GRID_SIZE)
    return x, y

def main():
    try:
        pygame.init()
        
       
        mole_image = pygame.image.load("mole.png")
        
       
        screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption("Whack-a-Mole")
        clock = pygame.time.Clock()
        
        # Initial mole position
        mole_x, mole_y = move_mole()
        
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Check for mouse click and if mole is clicked
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_pos = event.pos
                    mole_rect = pygame.Rect(mole_x, mole_y, GRID_SIZE, GRID_SIZE)
                    if mole_rect.collidepoint(mouse_pos):
                        mole_x, mole_y = move_mole()  # Move mole to a new position

         
            screen.fill(BACKGROUND_COLOR)
            
            
            draw_grid(screen)
            
          
            screen.blit(mole_image, mole_image.get_rect(topleft=(mole_x, mole_y)))
            
            # Update the display
            pygame.display.flip()
            clock.tick(60)
    finally:
        pygame.quit()

if __name__ == "__main__":
    main()
