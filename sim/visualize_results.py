"""
Post-run results plotting using Matplotlib.
Pass in the logger DataFrame after simulation completes.
"""

import matplotlib.pyplot as plt


def plot_results(log_df, title="Simulation Results"):
    if log_df is None or log_df.empty:
        print("No data to plot.")
        return

    numeric_cols = log_df.select_dtypes(include="number").columns.tolist()
    if "time" in numeric_cols:
        numeric_cols.remove("time")

    n = len(numeric_cols)
    if n == 0:
        print("No numeric columns to plot.")
        return

    fig, axes = plt.subplots(n, 1, figsize=(12, 3 * n), sharex=True)
    if n == 1:
        axes = [axes]

    for ax, col in zip(axes, numeric_cols):
        ax.plot(log_df["time"], log_df[col], linewidth=1.5)
        ax.set_ylabel(col, fontsize=9)
        ax.grid(True, alpha=0.4)

    axes[-1].set_xlabel("Time (s)")
    fig.suptitle(title, fontsize=14)
    plt.tight_layout()
    plt.savefig("results.png", dpi=150)
    plt.show()
    print("Results saved to results.png")
