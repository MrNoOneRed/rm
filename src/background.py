import pygame
from pygame import Surface

IMAGE_SRC = 'assets/bg.png'

class Background:
    def __init__(self, vx: float = 0.0, vy: float = 0.0):
        self.vx = vx
        self.vy = vy
        self.ox = 0.0
        self.oy = 0.0

        try:
            tile = pygame.image.load(IMAGE_SRC)

            if tile.get_alpha() is not None:
                self.tile = tile.convert_alpha()
            else:
                self.tile = tile.convert()
        except Exception as e:
            print(e)

        self.tw = self.tile.get_width()
        self.th = self.tile.get_height()

    def update(self, dt_sec: float) -> None:
        self.ox += self.vx * dt_sec
        self.oy += self.vy * dt_sec

        if self.tw > 0:
            self.ox = self.ox % self.tw
        if self.th > 0:
            self.oy = self.oy % self.th

    def draw(self, target: Surface) -> None:
        width, height = target.get_size()
        ox = -int(self.ox)
        oy = -int(self.oy)

        x = ox - self.tw
        while x < width:
            y = oy - self.th
            while y < height:
                target.blit(self.tile, (x, y))
                y += self.th
            x += self.tw