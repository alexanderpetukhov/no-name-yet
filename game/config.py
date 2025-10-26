import pygame as pg

from constants import (
    COLORS,
    INITIAL_TILE_SIZE,
    LIGHT_RADIUS,
    MIN_TILE_SIZE,
    SCREEN_SIZE,
    TILE_CHANGE_SIZE,
)


class Config:
    def __init__(self):
        self.screen_height = SCREEN_SIZE[0]
        self.screen_width = SCREEN_SIZE[1]
        self.tile_size = 0
        self.min_tile_size = MIN_TILE_SIZE
        self.tile_change_size = TILE_CHANGE_SIZE

        self.tiles_rows = 0
        self.row_offset = 0

        self.tiles_cols = 0
        self.col_offset = 0

        self.surfaces = dict()
        self.colors = COLORS
        self.light_radius = LIGHT_RADIUS

        self.set_tile_size(INITIAL_TILE_SIZE)

    @staticmethod
    def _calculate_tiles(size, tile_size):
        ratio = size // tile_size
        return ratio - (1 - ratio % 2)

    def set_tile_size(self, new_size):
        self.tile_size = new_size

        self.tiles_rows = self._calculate_tiles(self.screen_height, new_size)
        self.row_offset = (self.screen_height - self.tiles_rows * new_size) // 2

        self.tiles_cols = self._calculate_tiles(self.screen_width, new_size)
        self.col_offset = (self.screen_width - self.tiles_cols * new_size) // 2

        self._update_surfaces()

    def _update_surfaces(self):
        for key, color in self.colors.items():
            self.surfaces[key] = pg.Surface((self.tile_size, self.tile_size))
            self.surfaces[key].fill(color)
            pg.draw.rect(self.surfaces[key], (0, 0, 0), self.surfaces[key].get_rect(), 1)

    def advance_difficulty(self):
        if self.tile_size <= self.min_tile_size:
            return

        self.set_tile_size(self.tile_size - self.tile_change_size)


config = Config()
