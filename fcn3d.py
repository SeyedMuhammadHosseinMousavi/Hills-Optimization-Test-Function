import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Define the Simplified and Stable Pyramid Function
def pyramid_function(x):
    p = np.clip(x, -40.313, 40.313)  # Constrain variables
    term1 = np.sum(np.sin(p)) * 2  # Sinusoidal term
    term2 = np.sum(p ** 1) * 0.1    # Quadratic term for smoothness
    result = term1 + term2
    return result if np.isfinite(result) else 1e10  # Penalize invalid results

# Create a grid of values for visualization
x = np.linspace(-40.313, 40.313, 100)
y = np.linspace(-40.313, 40.313, 100)
X, Y = np.meshgrid(x, y)
Z = np.array([pyramid_function([xi, yi, 0, 0, 0, 0]) for xi, yi in zip(np.ravel(X), np.ravel(Y))])
Z = Z.reshape(X.shape)

# Plot the function
fig = plt.figure(figsize=(12, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='viridis', edgecolor='none')
ax.set_title("3D Visualization of the Pyramid Function")
ax.set_xlabel("X-axis")
ax.set_ylabel("Y-axis")
ax.set_zlabel("Pyramid Function Value")
plt.show()
