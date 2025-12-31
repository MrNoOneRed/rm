# file: menu_http_demo.py
import sys
import pygame

from pygame import Color
from background import Background

width = 800
height = 600
fps = 60


pygame.init()
window = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()
c_white = Color(255, 255, 255)
bg_speed = 20

running = True

bg = Background(bg_speed, bg_speed)

while running:
    dt_ms = clock.tick(fps)
    dt = dt_ms / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit(); sys.exit()

    window.fill((0, 0, 0))

    bg.update(dt)
    bg.draw(window)

    pygame.display.flip()

pygame.quit()
sys.exit()
