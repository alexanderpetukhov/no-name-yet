import asyncio


from constants import FPS
from game_core import (
    initialize_pygame,
    process_events,
    render_game,
)
from player import Player


async def main():
    screen, clock, all_sprites = initialize_pygame()
    player = Player()
    all_sprites.add(player)

    while process_events(player):
        all_sprites.update()
        render_game(screen, all_sprites)

        clock.tick(FPS)
        await asyncio.sleep(0)


if __name__ == '__main__':
    asyncio.run(main())
