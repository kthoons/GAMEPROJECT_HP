import os
import pygame

pygame.init()
screen_height = 720
screen_width = 448
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Puzzle Bobble")
clock = pygame.time.Clock()

# 배경 이미지 불러오기
current_path = os.path.dirname(__file__)
background = pygame.image.load(os.path.join(current_path, "background.png"))

# 구슬 만들기
bubbles = [
    pygame.image.load(os.path.join(current_path, "blue.png")),
    pygame.image.load(os.path.join(current_path, "yellow.png")),
    pygame.image.load(os.path.join(current_path, "green.png")),
    pygame.image.load(os.path.join(current_path, "purple.png")),
    pygame.image.load(os.path.join(current_path, "red.png")),
    pygame.image.load(os.path.join(current_path, "black.png"))
]













############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################
############################################################################################################

running = True
while running:
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(background, (0, 0))
    pygame.display.update()

pygame.quit()