import math
import time

import numpy as np

from simulated.config import (
    GRID_SIZE,
    MAX_ITERATIONS,
    MIN_TEMPERATURE,
    START_TEMPERATURE,
    STALL_LIMIT,
    TEMPERATURE_DECAY,
    TUNNEL_RADIUS,
    TUNNEL_STRENGTH,
)


def get_neighbors(position):
    """Return all valid 8-connected neighbours."""

    x, y = position
    neighbors = []

    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue

            nx = x + dx
            ny = y + dy

            if 0 <= nx < GRID_SIZE and 0 <= ny < GRID_SIZE:
                neighbors.append((nx, ny))

    return neighbors


def _tunnel_probability(delta_height, temperature):
    if delta_height <= 0:
        return 1.0

    thermal_factor = math.exp(-delta_height / max(temperature, 1e-9))
    tunneling_factor = math.exp(-delta_height / max(TUNNEL_STRENGTH, 1e-9))
    return min(1.0, thermal_factor + tunneling_factor)


def _tunnel_jump(terrain, current_position, temperature):
    x, y = current_position
    current_height = terrain[current_position]

    for _ in range(8):
        dx = int(np.random.randint(-TUNNEL_RADIUS, TUNNEL_RADIUS + 1))
        dy = int(np.random.randint(-TUNNEL_RADIUS, TUNNEL_RADIUS + 1))

        if dx == 0 and dy == 0:
            continue

        nx = np.clip(x + dx, 0, GRID_SIZE - 1)
        ny = np.clip(y + dy, 0, GRID_SIZE - 1)
        target = (int(nx), int(ny))
        target_height = terrain[target]

        delta_height = target_height - current_height
        if np.random.random() < _tunnel_probability(delta_height, temperature):
            return target

    return current_position


def simulated_quantum_annealing(terrain, start_position):
    """Quantum-annealing-inspired search with probabilistic tunneling moves."""

    current = start_position
    path = [current]
    iterations = 0
    stalled_steps = 0
    temperature = START_TEMPERATURE

    start_time = time.perf_counter()

    while iterations < MAX_ITERATIONS and temperature > MIN_TEMPERATURE:
        current_height = terrain[current]
        neighbors = get_neighbors(current)

        neighbor_heights = [(terrain[position], position) for position in neighbors]
        neighbor_heights.sort(key=lambda item: item[0])

        moved = False

        if neighbor_heights:
            best_height, best_position = neighbor_heights[0]
            delta_height = best_height - current_height

            accept_probability = _tunnel_probability(delta_height, temperature)

            if np.random.random() < accept_probability:
                current = best_position
                moved = True

        if not moved:
            tunnel_target = _tunnel_jump(terrain, current, temperature)
            if tunnel_target != current:
                current = tunnel_target
                moved = True

        if moved:
            path.append(current)
            stalled_steps = 0
        else:
            stalled_steps += 1

        iterations += 1
        temperature *= TEMPERATURE_DECAY

        if stalled_steps >= STALL_LIMIT:
            break

    end_time = time.perf_counter()

    return {
        "path": path,
        "iterations": iterations,
        "execution_time_ms": (end_time - start_time) * 1000,
        "final_position": current,
        "final_height": float(terrain[current]),
    }
