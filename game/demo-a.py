import asyncio

from config import config
from constants import FPS
from game_core import (
    initialize_pygame,
    process_events,
    render_game,
)
from player import Player


async def main():
    screen, clock = initialize_pygame()
    player = Player()
    entities = [player]

    while process_events(entities):
        render_game(screen)

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
