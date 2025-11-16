import pygame as pg
from pathlib import Path


GAME_PATH = Path(__file__).parent
PROJECT_PATH = GAME_PATH.parent
STATIC_PATH = PROJECT_PATH / "static"
SKINS_PATH = STATIC_PATH / "skins"
BACKGROUNDS_PATH = STATIC_PATH / "backgrounds"
BACKGROUNDS_FOLDER = str(STATIC_PATH / "backgrounds")
SKINS_FOLDER = str(SKINS_PATH)
DEFAULT_BACKGROUND = pg.image.load(str(BACKGROUNDS_PATH / "Basic_forest.png"))
CAPTION = 'George through the multiverse / Use AD keys for motion / SPACE to jump and E to shoot'
FPS = 25
SCREEN_SIZE = (1296, 768)

MOVES = {
    pg.K_d,
    pg.K_a,
    pg.K_e,
    pg.K_SPACE,
}