"""
Animated CLT demo: sample means of an exponential (skewed) distribution
become bell-shaped as the sample size n grows.
Requires: numpy, matplotlib, pillow
"""
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

rng = np.random.default_rng(42)
n_trials = 10_000
sample_sizes = [1, 2, 3, 5, 8, 12, 20, 30, 30, 30]  # last frames hold on n = 30

fig, ax = plt.subplots(figsize=(7, 4.2))

def update(frame):
    n = sample_sizes[frame]
    ax.clear()
    means = rng.exponential(scale=1.0, size=(n_trials, n)).mean(axis=1)
    ax.hist(means, bins=50, range=(0, 4), density=True, color="#2b6cb0", alpha=0.8)

    # Normal curve with the theoretical CLT mean and std (mean = 1, std = 1/sqrt(n))
    x = np.linspace(0, 4, 300)
    sigma = 1 / np.sqrt(n)
    ax.plot(x, np.exp(-0.5 * ((x - 1) / sigma) ** 2) / (sigma * np.sqrt(2 * np.pi)),
            color="crimson", lw=2, label="Normal curve")

    ax.set_xlim(0, 4)
    ax.set_ylim(0, 3.2)
    ax.set_title(f"Sample size n = {n}", fontsize=14)
    ax.set_xlabel("Sample mean")
    ax.set_ylabel("Density")
    ax.legend(loc="upper right")

anim = FuncAnimation(fig, update, frames=len(sample_sizes), interval=900)
anim.save("clt_animation.gif", writer=PillowWriter(fps=1.2), dpi=110)
print("Saved: clt_animation.gif")
