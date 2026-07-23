import numpy as np


def build_summary(times, iterations, heights, errors, global_height, success_count, overall_time_ms):
    return {
        "runs": len(times),
        "avg_time": float(np.mean(times)),
        "avg_iterations": float(np.mean(iterations)),
        "avg_height": float(np.mean(heights)),
        "avg_error": float(np.mean(errors)),
        "best_height": float(np.min(heights)),
        "worst_height": float(np.max(heights)),
        "global_minimum": float(global_height),
        "success_rate": 100.0 * success_count / len(times),
        "total_time_ms": float(overall_time_ms),
    }


def print_summary(summary):
    print("\n========== Simulated Quantum Annealing ==========\n")
    print(f"Runs                 : {summary['runs']}")
    print(f"Average Time         : {summary['avg_time']:.4f} ms")
    print(f"Average Iterations   : {summary['avg_iterations']:.2f}")
    print(f"Average Height       : {summary['avg_height']:.4f}")
    print(f"Average Error        : {summary['avg_error']:.4f}")
    print()
    print(f"Best Height          : {summary['best_height']:.4f}")
    print(f"Worst Height         : {summary['worst_height']:.4f}")
    print()
    print(f"Global Minimum       : {summary['global_minimum']:.4f}")
    print(f"Success Rate         : {summary['success_rate']:.2f}%")
    print()
    print(f"Total Time Taken     : {summary['total_time_ms']:.2f} ms")
