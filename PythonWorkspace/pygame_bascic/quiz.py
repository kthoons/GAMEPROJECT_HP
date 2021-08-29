import pygame 
from random import *

#####################################################################
# 기본 초기화 (반드시 해야 하는 것들)
pygame.init() #초기화 (반드시 필요)

# 화면 크기 설정
screen_width = 480 # 가로 크기
screen_height = 640 # 세로 크기
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 타이틀 설정
pygame.display.set_caption("balloon스퍼거 피하기 게임") # 게임 이름

# FPS
clock = pygame.time.Clock()
#####################################################################

# 1. 사용자 게임 초기화 (배경 화면, 게임 이미지, 좌표, 속도, 폰트 등)

background = pygame.image.load("C:\\Users\\강태훈\\Desktop\\PythonWorkspace\\pygame_bascic\\게임배경.jpg")

character = pygame.image.load("C:\\Users\\강태훈\\Desktop\\PythonWorkspace\\pygame_bascic\\강태훈.jpg")
character_size = character.get_rect().size  
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width / 2) - (character_width / 2)
character_y_pos = screen_height - character_height



enemy = pygame.image.load("C:\\Users\\강태훈\\Desktop\\PythonWorkspace\\pygame_bascic\\balloon스퍼거.jpg")
enemy_size = enemy.get_rect().size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = randint(0, screen_width - enemy_width)
enemy_y_pos = 0
enemy_speed = 0.6


to_x = 0
character_speed = 0.1

running = True # 게임이 진행중인가?
while running:
    dt = clock.tick(200) # 게임화면의 초당 프레임 수를 설정

    # 2. 이벤트 처리 (키보드, 마우스 등)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if event.type == pygame.KEYDOWN :
        if event.key == pygame.K_LEFT :
            to_x -= character_speed
        elif event.key == pygame.K_RIGHT :
            to_x += character_speed
        
    if event.type == pygame.KEYUP :
        if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT :
            to_x = 0

    # 3. 게임 캐릭터 위치 정의

    character_x_pos += to_x * dt

    screen.blit(background, (0,0))
    screen.blit(character, (character_x_pos, character_y_pos))
    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))

    enemy_y_pos += enemy_speed * dt

    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if enemy_y_pos > screen_height :
        enemy_x_pos = randint(0, screen_width - enemy_width)
        enemy_y_pos = 0
    
    
    # 4. 충돌 처리

    character_rect = character.get_rect() 
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    if character_rect.colliderect(enemy_rect):
        print("게임오버.")
        running = False

    # 5. 화면에 그리기

    pygame.display.update()

pygame.quit()