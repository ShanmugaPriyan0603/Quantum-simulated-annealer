import os
import time

import numpy as np

if __package__ is None or __package__ == "":
    import sys

    sys.path.append(os.path.dirname(os.path.dirname(__file__)))

from simulated.bicycle import simulated_quantum_annealing
from simulated.config import GRID_SIZE, NUM_RUNS, RANDOM_SEED
from simulated.metrics import build_summary, print_summary
from simulated.terrain import generate_terrain
from simulated.visualize import plot_results


def main():
    np.random.seed(RANDOM_SEED)

    terrain = generate_terrain()
    global_height = float(terrain.min())

    times = []
    iterations = []
    errors = []
    heights = []

    success = 0

    overall_start = time.perf_counter()

    for _ in range(NUM_RUNS):
        start = (
            int(np.random.randint(0, GRID_SIZE)),
            int(np.random.randint(0, GRID_SIZE)),
        )

        result = simulated_quantum_annealing(terrain, start)

        times.append(result["execution_time_ms"])
        iterations.append(result["iterations"])
        heights.append(result["final_height"])

        error = abs(result["final_height"] - global_height)
        errors.append(error)

        if error < 1e-6:
            success += 1

    overall_end = time.perf_counter()
    overall_time_ms = (overall_end - overall_start) * 1000

    summary = build_summary(
        times,
        iterations,
        heights,
        errors,
        global_height,
        success,
        overall_time_ms,
    )

    print_summary(summary)
    plot_results(heights, iterations, times, errors)


if __name__ == "__main__":
    main()
