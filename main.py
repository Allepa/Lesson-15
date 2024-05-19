import pygame
import random
from pygame.color import THECOLORS

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Игра Тир")
icon = pygame.image.load("img/Тир.jpg")
pygame.display.set_icon(icon)
target = pygame.image.load("img/apple.png")
target_width = 80
target_height = 80
target_x = random.randint(0, SCREEN_WIDTH - target_width)
target_y = random.randint(0, SCREEN_HEIGHT - target_height)
color = (random.randint(0,255), random.randint(0,255), random.randint(0,255))
score = 0
font = pygame.font.Font(None, 36)
text = font.render(str(''), True, THECOLORS['red'])

running = True
while running:
    screen.fill(color)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x, mouse_y = pygame.mouse.get_pos()
            if mouse_x >= target_x and mouse_x <= target_x + target_width and mouse_y >= target_y and mouse_y <= target_y + target_height:
                target_x = random.randint(0, SCREEN_WIDTH - target_width)
                target_y = random.randint(0, SCREEN_HEIGHT - target_height)
                color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
                score += 1
                font = pygame.font.SysFont('couriernew', 40)
                Mytext = str('Попал ') + str(score) + str(' раз!')
                text = font.render(Mytext, True, THECOLORS['red'])
    screen.blit(text, (50, 50))
    screen.blit(target, (target_x, target_y))
    pygame.display.update()
pygame.quit()
