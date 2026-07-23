import time
import numpy as np

from visualize import plot_results
from terrain import generate_terrain
from bicycle import hill_climb
from config import GRID_SIZE, NUM_RUNS

terrain = generate_terrain()

global_height = terrain.min()

global_position = np.unravel_index(
    np.argmin(terrain),
    terrain.shape
)

times = []
iterations = []
errors = []
heights = []

success = 0

overall_start = time.perf_counter()

for _ in range(NUM_RUNS):

    start = (
        np.random.randint(0, GRID_SIZE),
        np.random.randint(0, GRID_SIZE)
    )

    result = hill_climb(terrain, start)

    times.append(result["execution_time_ms"])
    iterations.append(result["iterations"])
    heights.append(result["final_height"])

    error = abs(result["final_height"] - global_height)
    errors.append(error)

    if error < 1e-6:
        success += 1

overall_end = time.perf_counter()
median_height = np.median(heights)
std_height = np.std(heights)

print("\n========== Classical Hill Climbing ==========\n")

print(f"Median Height       : {median_height:.4f}")
print(f"Std Dev Height      : {std_height:.4f}")

print(f"Minimum Height      : {np.min(heights):.4f}")
print(f"Maximum Height      : {np.max(heights):.4f}")

print(f"25th Percentile     : {np.percentile(heights,25):.4f}")
print(f"75th Percentile     : {np.percentile(heights,75):.4f}")

print(f"95th Percentile     : {np.percentile(heights,95):.4f}")

print(f"Runs                 : {NUM_RUNS}")
print(f"Average Time         : {np.mean(times):.4f} ms")
print(f"Average Iterations   : {np.mean(iterations):.2f}")
print(f"Average Height       : {np.mean(heights):.4f}")
print(f"Average Error        : {np.mean(errors):.4f}")

print()

print(f"Best Height          : {np.min(heights):.4f}")
print(f"Worst Height         : {np.max(heights):.4f}")

print()

print(f"Global Minimum       : {global_height:.4f}")
print(f"Success Rate         : {100*success/NUM_RUNS:.2f}%")

print()

print(f"Total Benchmark Time : {(overall_end-overall_start)*1000:.2f} ms")

plot_results(
    heights,
    iterations,
    times
)