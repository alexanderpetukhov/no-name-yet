from enum import (
    IntEnum,
    auto,
)

import pygame as pg


class FOG(IntEnum):
    DARK = auto()
    KNOWN = auto()
    LIT = auto()


class TILES(IntEnum):
    FLOOR = auto()
    WALL = auto()
    PLAYER = auto()
    EXIT = auto()


CAPTION = 'Cave Explorer PC game / Use WASD keys'
FPS = 8
SCREEN_SIZE = (600, 600)
INITIAL_TILE_SIZE = 34
MIN_TILE_SIZE = 10
TILE_CHANGE_SIZE = 3
LIGHT_RADIUS = 3.2

FOG_OFFSET = 100
MOVE_TILES = {TILES.FLOOR, TILES.EXIT}
FOG_TILES = {TILES.FLOOR, TILES.WALL, TILES.EXIT}

COLORS = {
    TILES.FLOOR: (90, 90, 180),
    TILES.FLOOR + FOG_OFFSET: (45, 45, 90),
    TILES.WALL: (120, 120, 120),
    TILES.WALL + FOG_OFFSET: (60, 60, 60),
    TILES.PLAYER: (255, 0, 0),
    TILES.EXIT: (0, 255, 0),
    TILES.EXIT + FOG_OFFSET: (0, 120, 0),
}

MOVES = {
    pg.K_w: (-1, 0),
    pg.K_a: (0, -1),
    pg.K_s: (1, 0),
    pg.K_d: (0, 1),
}

POPULATION_PER_SEED = 90
