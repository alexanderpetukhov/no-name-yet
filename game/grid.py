from copy import deepcopy
from math import dist
from random import (
    randint,
    sample,
    shuffle,
)

from config import config
from constants import (
    FOG,
    LIGHT_RADIUS,
    MOVES,
    POPULATION_PER_SEED,
    TILES,
)


def update_fog(fog, player_row, player_col):
    player_position = (player_col, player_row)

    for row in range(config.tiles_rows):
        for col in range(config.tiles_cols):
            distance = dist((row, col), player_position)

            if distance <= LIGHT_RADIUS:
                fog[row][col] = FOG.LIT
                continue

            if fog[row][col] == FOG.LIT:
                fog[row][col] = FOG.KNOWN


def generate_initial_grid():
    grid = [
        [TILES.WALL] * config.tiles_cols
        for _ in range(config.tiles_rows)
    ]
    fog = [
        [FOG.DARK] * config.tiles_cols
        for _ in range(config.tiles_rows)
    ]

    middle_row = config.tiles_rows // 2
    middle_col = config.tiles_cols // 2
    middle = (middle_row, middle_col)

    floor_radius = min(middle_row, middle_col) // 2 + 1

    for row in range(config.tiles_rows):
        for col in range(config.tiles_cols):
            if dist((row, col), middle) < floor_radius:
                grid[row][col] = TILES.FLOOR

    grid[middle_row][middle_col] = TILES.PLAYER
    grid[middle_row - floor_radius][middle_col] = TILES.EXIT

    update_fog(fog, *middle)

    return grid, fog, middle


def generate_seeds():
    seeds = set()

    population = config.tiles_rows * config.tiles_cols
    seeds_needed = population // POPULATION_PER_SEED

    while len(seeds) < seeds_needed:
        row = randint(1, config.tiles_rows - 2)
        col = randint(1, config.tiles_cols - 2)
        seeds.add((row, col))

    return seeds


def generate_edges(seeds_set: set[tuple[int]]):
    seeds = list(seeds_set)
    unused_seeds = None

    size = len(seeds_set)
    edges: set[tuple[tuple[int]]] = set()

    min_edges_number = size - 1
    max_edges_number = size * (size - 1) // 2

    edges_number = randint(min_edges_number, max_edges_number)
    pair: set[tuple[int]] = set()

    while len(edges) < edges_number:
        if not unused_seeds:
            unused_seeds = seeds[:]
            shuffle(unused_seeds)

        new_seed = unused_seeds.pop()

        if new_seed not in pair:
            pair.add(new_seed)

        if len(pair) == 2:
            edges.add(tuple(pair))
            pair = set()

    return edges


def paint_edge(grid, edge):
    node_a, node_b = edge
    row_a, col_a = node_a
    row_b, col_b = node_b

    row_distance = abs(row_b - row_a)
    row_direction = 1 if row_a < row_b else -1
    row = row_a

    col_distance = abs(col_b - col_a)
    col_direction = 1 if col_a < col_b else -1
    col = col_a

    top_distance = max(row_distance, col_distance)
    row_step = row_distance / top_distance * row_direction
    col_step = col_distance / top_distance * col_direction

    while True:
        row_int = round(row)
        col_int = round(col)
        grid[row_int][col_int] = TILES.FLOOR

        if (row_int, col_int) == (row_b, col_b):
            break

        row += row_step
        col += col_step


def paint_edges(grid, edges):
    for edge in edges:
        paint_edge(grid, edge)


def boldify_floors(grid):
    old_grid = deepcopy(grid)

    for row in range(1, config.tiles_rows - 1):
        for col in range(1, config.tiles_cols - 1):
            if old_grid[row][col] == TILES.FLOOR:
                continue

            for row_shift, col_shift in MOVES.values():
                new_row = row + row_shift
                new_col = col + col_shift

                if old_grid[new_row][new_col] == TILES.FLOOR:
                    grid[row][col] = TILES.FLOOR
                    continue


def place_player_and_exit(grid):
    targets = list()

    for row in range(1, config.tiles_rows - 1):
        for col in range(1, config.tiles_cols - 1):
            if grid[row][col] == TILES.FLOOR:
                targets.append((row, col))

    indexes = sample(range(len(targets)), 2)

    player_position = targets[indexes[0]]
    row, col = player_position
    grid[row][col] = TILES.PLAYER

    row, col = targets[indexes[1]]
    grid[row][col] = TILES.EXIT

    return player_position


def generate_next_level():
    grid = [
        [TILES.WALL] * config.tiles_cols
        for _ in range(config.tiles_rows)
    ]
    fog = [
        [FOG.DARK] * config.tiles_cols
        for _ in range(config.tiles_rows)
    ]
    seeds = generate_seeds()
    edges = generate_edges(seeds)
    paint_edges(grid, edges)
    boldify_floors(grid)
    # boldify_floors(grid)
    player_position = place_player_and_exit(grid)
    update_fog(fog, *player_position)

    return grid, fog, player_position
