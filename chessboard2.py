import pygame
def board():   
    width=480
    height=480
    block_size=59
    window = pygame.display.set_mode((width,height))
    background_color = (0,0,0)
    window.fill(background_color)
    for y in range(height):
        for x in range(width):
            rect = pygame.Rect(x*(block_size+1), y*(block_size+1), block_size, block_size)
            pygame.draw.rect(window, (255,255,255), rect)
    pygame.display.flip()
board()

# It's just the board