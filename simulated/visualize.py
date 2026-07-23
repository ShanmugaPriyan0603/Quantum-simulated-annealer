from pathlib import Path

import matplotlib.pyplot as plt


def plot_results(heights, iterations, times, errors):
    output_dir = Path("Results")
    output_dir.mkdir(exist_ok=True)

    figure_path = output_dir / "simulated_quantum_annealing_distributions.png"

    fig, axes = plt.subplots(2, 2, figsize=(12, 10))
    fig.suptitle("Simulated Quantum Annealing Distributions", fontsize=16)

    axes[0, 0].hist(heights, bins=40, edgecolor="black", color="#2c7fb8")
    axes[0, 0].set_title("Final Heights")
    axes[0, 0].set_xlabel("Height")
    axes[0, 0].set_ylabel("Frequency")
    axes[0, 0].grid(alpha=0.25)

    axes[0, 1].hist(iterations, bins=30, edgecolor="black", color="#7fcdbb")
    axes[0, 1].set_title("Iterations")
    axes[0, 1].set_xlabel("Iterations")
    axes[0, 1].set_ylabel("Frequency")
    axes[0, 1].grid(alpha=0.25)

    axes[1, 0].hist(errors, bins=40, edgecolor="black", color="#fdae61")
    axes[1, 0].set_title("Errors")
    axes[1, 0].set_xlabel("Absolute Error")
    axes[1, 0].set_ylabel("Frequency")
    axes[1, 0].grid(alpha=0.25)

    axes[1, 1].hist(times, bins=40, edgecolor="black", color="#d7191c")
    axes[1, 1].set_title("Execution Times")
    axes[1, 1].set_xlabel("Time (ms)")
    axes[1, 1].set_ylabel("Frequency")
    axes[1, 1].grid(alpha=0.25)

    plt.tight_layout(rect=(0, 0, 1, 0.96))
    plt.savefig(figure_path, dpi=200, bbox_inches="tight")
    plt.show()
