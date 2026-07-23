import time
import numpy as np

from Classical.config import GRID_SIZE


def get_neighbors(position):
    """
    Returns all valid 8-connected neighbours.
    """

    x, y = position
    neighbors = []

    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:

            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                neighbors.append((nx, ny))

    return neighbors


def hill_climb(terrain, start_position):
    """
    Classical greedy hill climbing.
    Always moves to the lowest neighbouring cell.
    """

    current = start_position

    path = [current]

    iterations = 0

    start_time = time.perf_counter()

    while True:

        current_height = terrain[current]

        neighbors = get_neighbors(current)

        # Find lowest neighbour
        best_neighbor = current
        best_height = current_height

        for n in neighbors:

            h = terrain[n]

            if h < best_height:
                best_height = h
                best_neighbor = n

        # No lower neighbour -> local minimum
        if best_neighbor == current:
            break

        current = best_neighbor
        path.append(current)

        iterations += 1

    end_time = time.perf_counter()

    return {
        "path": path,
        "iterations": iterations,
        "execution_time_ms": (end_time - start_time) * 1000,
        "final_position": current,
        "final_height": terrain[current]
    }