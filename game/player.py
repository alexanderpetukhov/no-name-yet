import pygame as pg

from game.constants import (
    SKINS_PATH,
    PLAYER_START,
    PLAYER_X_SPEED,
    SCREEN_SIZE,
    GRAVITY_ACCELERATION,
    PLAYER_JUMP_SPEED,
    RED_COLOR,
    SHOW_COLLISIONS,
    HORIZON_Y,
)


class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pg.image.load(str(SKINS_PATH / "hero right.png"))
        self.image_facing_left = pg.transform.flip(self.image, True, False)
        self.image_facing_right = self.image
        self.rect = self.image.get_rect()

        self.rect.midtop = PLAYER_START
        self.collision_rect = self.rect.inflate(-16, -16)

        self.x_speed = 0
        self.y_speed = 100
        self.y_acceleration = 0

        self.going_right = False
        self.going_left = False

    def move(self, pressed_key, event_type):
        if pg.K_d == pressed_key:
            self.going_right = event_type == pg.KEYDOWN

        if pg.K_a == pressed_key:
            self.going_left = event_type == pg.KEYDOWN

        if self.going_right and not self.going_left:
            self.x_speed = PLAYER_X_SPEED
            self.image = self.image_facing_right
        elif self.going_left and not self.going_right:
            self.x_speed = -PLAYER_X_SPEED
            self.image = self.image_facing_left
        else:
            self.x_speed = 0

        if pg.K_SPACE == pressed_key:
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

        if SHOW_COLLISIONS:
            pg.draw.rect(surface, RED_COLOR, self.collision_rect, 2)
