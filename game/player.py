import pygame as pg

from constants import (
    SKINS_PATH,
    PLAYER_START,
    SCREEN_SIZE,
    GRAVITY_ACCELERATION,
    PLAYER_JUMP_SPEED,
)
from game.constants import HORIZON_Y


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pg.image.load(str(SKINS_PATH / "hero right.png"))
        self.image_facing_left = pg.transform.flip(self.image, True, False)
        self.image_facing_right = self.image
        self.rect = self.image.get_rect()
        self.rect.midtop = PLAYER_START
        self.collision_rect = self.rect.inflate(-16, -16)
        self.show_collision = True
        self.x_speed = 0
        self.y_speed = 100
        self.y_acceleration = 0

    def move(self, pressed_key, event_type):
        if pg.K_d == pressed_key:
            if event_type == pg.KEYDOWN:
                self.x_speed = 10
                self.image = self.image_facing_right
            else:
                self.x_speed = 0
        elif pg.K_a == pressed_key:
            if event_type == pg.KEYDOWN:
                self.x_speed = -10
                self.image = self.image_facing_left
            else:
                self.x_speed = 0

        elif pg.K_SPACE == pressed_key:
            if event_type == pg.KEYDOWN:
                self.y_speed -= PLAYER_JUMP_SPEED


    def update(self):
        self.rect.x += self.x_speed

        if self.rect.right > SCREEN_SIZE[0]:
            self.rect.right = SCREEN_SIZE[0]

        if self.rect.left < 0:
            self.rect.left = 0

        self.y_acceleration += GRAVITY_ACCELERATION
        self.y_speed += GRAVITY_ACCELERATION
        self.rect.y += self.y_speed

        if self.rect.top > HORIZON_Y:
            self.rect.top = HORIZON_Y
            self.y_speed = 0
            self.y_acceleration = 0
        self.collision_rect.center = self.rect.center

    def draw(self, surface):
        surface.blit(self.image, self.rect)

        if self.show_collision:
            pg.draw.rect(surface, (255, 0, 0), self.collision_rect, 2)
