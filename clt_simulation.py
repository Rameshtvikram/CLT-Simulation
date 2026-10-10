"""
Central Limit Theorem demo: skewed data -> bell-shaped sample means.
Requires: numpy, seaborn, matplotlib
"""
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
sns.set_theme(style="whitegrid")

# 1) CLT: means of samples drawn from a heavily skewed (exponential) distribution
sample_sizes = [1, 2, 5, 30]
n_trials = 10_000

fig, axes = plt.subplots(1, 4, figsize=(16, 3.8), sharey=False)
for ax, n in zip(axes, sample_sizes):
    means = rng.exponential(scale=1.0, size=(n_trials, n)).mean(axis=1)
    sns.histplot(means, bins=50, kde=True, stat="density", ax=ax, color="#2b6cb0")
    ax.set_title(f"Sample size n = {n}")
    ax.set_xlabel("Sample mean")
fig.suptitle("Averages of a skewed distribution become bell-shaped as n grows", y=1.05)
plt.tight_layout()
plt.savefig("clt_simulation.png", dpi=200, bbox_inches="tight")
plt.close()

# 2) Transformation vs CLT: log transform makes skewed data approximately normal
income_like = rng.lognormal(mean=10, sigma=0.9, size=50_000)
fig, axes = plt.subplots(1, 2, figsize=(11, 3.8))
sns.histplot(income_like, bins=80, ax=axes[0], color="#c05621")
axes[0].set_title("Income-like data: right-skewed")
sns.histplot(np.log(income_like), bins=80, ax=axes[1], color="#2f855a")
axes[1].set_title("Log transform: skewed data -> approximately normal")
plt.tight_layout()
plt.savefig("not_everything_is_normal.png", dpi=200, bbox_inches="tight")
plt.close()

print("Saved: clt_simulation.png, not_everything_is_normal.png")
