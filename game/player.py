import pygame as pg

from constants import (
    SKINS_PATH,
    PLAYER_START,
)

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(str(SKINS_PATH / "hero right.png"))
        self.rect = self.image.get_rect()
        self.rect.midtop = PLAYER_START
        self.collision_rect = self.rect.inflate(-20, -20)
        self.show_collision = True

    def move(self, pressed_key):
        pass

    def update(self):
        self.collision_rect.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.show_collision:
            pg.draw.rect(surface, (255, 0, 0), self.collision_rect, 2)
