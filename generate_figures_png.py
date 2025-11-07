import numpy as np
import matplotlib.pyplot as plt

# Parameters (SI-like)
sigma0 = 1.0
xmax = 12.0
nx = 2000
x = np.linspace(-xmax, xmax, nx)

# Initial Gaussian psi and density
psi0 = (1.0 / (2 * np.pi * sigma0**2)**0.25) * np.exp(-x**2 / (4 * sigma0**2))
rho0 = np.abs(psi0)**2

fig, ax = plt.subplots(figsize=(7.2, 4.0), dpi=300)
ax.plot(x, rho0, label=r"$|\psi|^2$ (Gaussian)")
ax.set_xlabel("x")
ax.set_ylabel("density")
ax.set_title("Baseline density used in morphing examples")
ax.legend()
fig.tight_layout()
fig.savefig("figures/figure_baseline_density.png")
print("Saved: figures/figure_baseline_density.png")
