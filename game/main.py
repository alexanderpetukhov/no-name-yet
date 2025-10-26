import asyncio

from config import config
from constants import FPS
from game_core import (
    initialize_pygame,
    process_events,
    render_game,
)
from grid import (
    generate_initial_grid,
    generate_next_level,
)
from player import Player


async def main():
    screen, clock = initialize_pygame()
    grid, fog, position = generate_initial_grid()
    player = Player(*position)

    while process_events(player, grid, fog):
        render_game(screen, grid, fog)

        if player.win:
            config.advance_difficulty()
            grid, fog, position = generate_next_level()
            player.set_position(*position)
            player.win = False

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
