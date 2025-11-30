from functools import cache

import pygame as pg

from game.constants import (
    MOVES,
    CAPTION,
    SCREEN_SIZE,
    SCREEN_START,
    DEFAULT_BACKGROUND,
)


def initialize_pygame():
    pg.init()
    screen: pg.Surface = pg.display.set_mode(SCREEN_SIZE)
    clock = pg.time.Clock()
    all_sprites = pg.sprite.Group()

    screen.fill('black')
    screen.blit(DEFAULT_BACKGROUND, SCREEN_START)
    pg.display.set_caption(CAPTION)
    pg.display.update()

    return screen, clock, all_sprites


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


def process_events(player):
    is_running = True

    for event in pg.event.get():
        event_key = event.key if hasattr(event, 'key') else None

        if is_quit_event(event.type, event_key):
            is_running = False
            pg.quit()

        if is_move_event(event.type, event_key):
            player.move(event_key, event.type)

    return is_running


def render_game(screen, all_sprites):
    screen.blit(DEFAULT_BACKGROUND, SCREEN_START)

    for sprite in all_sprites:
        sprite.draw(screen)

    pg.display.flip()
