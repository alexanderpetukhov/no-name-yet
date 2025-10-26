from functools import cache

import pygame as pg

from config import config
from constants import (
    CAPTION,
    FOG,
    FOG_OFFSET,
    FOG_TILES,
    MOVES,
    SCREEN_SIZE,
)
from grid import update_fog


def initialize_pygame():
    pg.init()
    screen: pg.Surface = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()

    screen.fill('black')  # https://www.pygame.org/docs/ref/color_list.html
    pg.display.set_caption(CAPTION)
    pg.display.update()

    return screen, clock


@cache
def is_quit_event(event_type, event_key):
    if event_type == pg.QUIT:
        return True

    if event_type == pg.KEYDOWN and event_key == pg.K_ESCAPE:
        return True

    return False


@cache
def is_move_event(event_type, event_key):
    if event_type not in {pg.KEYDOWN, pg.KEYUP}:
        return False

    return event_key in MOVES


def process_events(player, grid, fog):
    is_running = True

    for event in pg.event.get():
        event_key = event.key if hasattr(event, 'key') else None

        if is_quit_event(event.type, event_key):
            is_running = False
            pg.quit()

        if is_move_event(event.type, event_key):
            player.examine_move_event(event.type, event_key)

    player.move(grid)

    if player.has_moved:
        update_fog(fog, player.row, player.col)

    return is_running


def render_game(screen, grid, fog):
    screen.fill('black')

    row_pixel = -config.tile_size + config.row_offset

    for row in range(config.tiles_rows):
        row_pixel += config.tile_size
        col_pixel = -config.tile_size + config.col_offset

        for col in range(config.tiles_cols):
            col_pixel += config.tile_size

            if fog[row][col] == FOG.DARK:
                continue

            entity_value = grid[col][row]

            if entity_value in FOG_TILES and fog[row][col] == FOG.KNOWN:
                entity_value += FOG_OFFSET

            surface = config.surfaces[entity_value]
            screen.blit(surface, (row_pixel, col_pixel))

    pg.display.flip()
