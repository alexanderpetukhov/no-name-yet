import pygame as pg

from constants import (
    MOVE_TILES,
    MOVES,
    TILES,
)


class Player:
    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.win = False
        self.keys_status = {key: False for key in MOVES}
        self.has_moved = False

    def examine_move_event(self, event_type, event_key):
        if event_type == pg.KEYUP:
            self.keys_status[event_key] = False
        else:
            self.keys_status[event_key] = True

    def move(self, grid):
        active_keys = [key for key, is_active in self.keys_status.items() if is_active]

        if not active_keys:
            self.has_moved = False
            return

        new_row, new_col = self.row, self.col

        for key in active_keys:
            row_shift, col_shift = MOVES[key]
            new_row += row_shift
            new_col += col_shift

        if grid[new_row][new_col] not in MOVE_TILES:
            self.has_moved = False
            return

        if grid[new_row][new_col] == TILES.EXIT:
            self.win = True

        grid[new_row][new_col] = TILES.PLAYER
        grid[self.row][self.col] = TILES.FLOOR
        self.row = new_row
        self.col = new_col

        self.has_moved = True

    def set_position(self, new_row, new_col):
        self.row = new_row
        self.col = new_col
