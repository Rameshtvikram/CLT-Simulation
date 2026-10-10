"""Central Limit Theorem demonstration.

Sample means of non-normal distributions become approximately normal
as the sample size n increases.
"""
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

rng = np.random.default_rng(42)

N_SAMPLES = 10_000          # number of sample means drawn per plot
SAMPLE_SIZES = [1, 5, 30, 100]

distributions = {
    "Exponential": lambda size: rng.exponential(scale=2.0, size=size),
    "Uniform": lambda size: rng.uniform(0, 10, size=size),
    "Binomial": lambda size: rng.binomial(n=10, p=0.2, size=size),
}

fig, axes = plt.subplots(
    len(distributions), len(SAMPLE_SIZES), figsize=(16, 9), constrained_layout=True
)

for row, (name, draw) in enumerate(distributions.items()):
    for col, n in enumerate(SAMPLE_SIZES):
        means = draw((N_SAMPLES, n)).mean(axis=1)
        ax = axes[row, col]
        ax.hist(means, bins=40, density=True, color="#4C72B0", alpha=0.75)

        # Overlay the normal curve fitted to the sample means
        mu, sigma = means.mean(), means.std()
        x = np.linspace(means.min(), means.max(), 200)
        ax.plot(x, stats.norm.pdf(x, mu, sigma), color="crimson", lw=2)

        ax.set_title(f"{name} | n = {n}")
        if col == 0:
            ax.set_ylabel("Density")

fig.suptitle("Central Limit Theorem: distribution of sample means", fontsize=16)
plt.savefig("clt_demo.png", dpi=150)
plt.show()
