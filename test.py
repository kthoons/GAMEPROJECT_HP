import pygame
import os
import time
pygame.init()
screen_width = 669  
screen_height = 569
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Running_test")
clock = pygame.time.Clock()

# 이미지 불러오기
current_path = os.path.dirname(__file__)
running_image = [
    pygame.image.load(os.path.join(current_path, "redhatfiles\png\Run (1).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\png\Run (2).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\png\Run (3).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\png\Run (4).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\png\Run (5).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\Png\Run (6).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\Png\Run (7).png")),
    pygame.image.load(os.path.join(current_path, "redhatfiles\Png\Run (8).png")),
]

running = True
while running:
    clock.tick(60) # FPS 60 으로 설정

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    for img in running_image:
        screen.blit(img, (0,0))
        time.sleep(0.5)

    pygame.display.update()

pygame.quit()

