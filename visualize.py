# visualize.py

import matplotlib.pyplot as plt


def plot_results(heights, iterations, times):

    # -------------------------------
    # Histogram of final heights
    # -------------------------------
    plt.figure(figsize=(8,5))

    plt.hist(
        heights,
        bins=40,
        edgecolor="black"
    )

    plt.xlabel("Final Height")
    plt.ylabel("Frequency")
    plt.title("Distribution of Final Heights")

    plt.grid(alpha=0.3)

    # -------------------------------
    # Histogram of iterations
    # -------------------------------
    plt.figure(figsize=(8,5))

    plt.hist(
        iterations,
        bins=30,
        edgecolor="black"
    )

    plt.xlabel("Iterations")
    plt.ylabel("Frequency")
    plt.title("Distribution of Iterations")

    plt.grid(alpha=0.3)

    # -------------------------------
    # Time vs Height
    # -------------------------------
    plt.figure(figsize=(8,5))

    plt.scatter(
        times,
        heights,
        s=10,
        alpha=0.5
    )

    plt.xlabel("Execution Time (ms)")
    plt.ylabel("Final Height")
    plt.title("Execution Time vs Final Height")

    plt.grid(alpha=0.3)

    plt.show()