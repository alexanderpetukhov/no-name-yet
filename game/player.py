import pygame as pg
from constants import SKINS_PATH

class Player:
    def __init__(self):
        self.sprite = pg.image.load(str(SKINS_PATH / "hero right.png"))

    def move(self, pressed_key):
        pass

    def update(self):
        pass