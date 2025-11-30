import pygame as pg
from pathlib import Path


GAME_PATH = Path(__file__).parent
PROJECT_PATH = GAME_PATH.parent
STATIC_PATH = PROJECT_PATH / "static"
SKINS_PATH = STATIC_PATH / "skins"
BACKGROUNDS_PATH = STATIC_PATH / "backgrounds"
BACKGROUNDS_FOLDER = str(STATIC_PATH / "backgrounds")
SKINS_FOLDER = str(SKINS_PATH)

CAPTION = 'George through the multiverse / Use AD keys for motion / SPACE to jump and E to shoot'
FPS = 25
SCREEN_SIZE = (1296, 768)
SCREEN_START = (0, 0)
HORIZON_Y = 626
PLAYER_START = (648, HORIZON_Y - 300)

SHOW_COLLISIONS = True

PLAYER_X_SPEED = 10
GRAVITY_ACCELERATION = 7
PLAYER_JUMP_SPEED = 90

DEFAULT_BACKGROUND_UNSCALED = pg.image.load(str(BACKGROUNDS_PATH / "Basic_forest.png"))
DEFAULT_BACKGROUND = pg.transform.scale(DEFAULT_BACKGROUND_UNSCALED, SCREEN_SIZE)

RED_COLOR = (255, 0, 0)

MOVES = {
    pg.K_d,
    pg.K_a,
    pg.K_e,
    pg.K_SPACE,
}