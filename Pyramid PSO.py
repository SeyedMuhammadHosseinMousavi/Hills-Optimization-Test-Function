import numpy as np
import matplotlib.pyplot as plt

# Define the Pyramid Function
def pyramid_function(x):
    p = np.clip(x, -40.313, 40.313)  # Constrain variables
    term1 = np.sum(np.sin(p)) * 10  # Sinusoidal term
    term2 = np.sum(p ** 2) * 0.1    # Quadratic term for smoothness
    result = term1 + term2
    return result if np.isfinite(result) else 1e10  # Penalize invalid results

# PSO Parameters
num_particles = 50
num_iterations = 100
dimensions = 6
lower_bound = -40.313
upper_bound = 40.313

# Initialize particles
particles = np.random.uniform(low=lower_bound, high=upper_bound, size=(num_particles, dimensions))
velocities = np.random.uniform(low=-1, high=1, size=(num_particles, dimensions))
personal_best_positions = particles.copy()
personal_best_scores = np.array([pyramid_function(p) for p in particles])
global_best_position = personal_best_positions[np.argmin(personal_best_scores)]
global_best_score = np.min(personal_best_scores)

# Store iteration costs
iteration_costs = []

# PSO Main Loop
for iteration in range(num_iterations):
    for i in range(num_particles):
        # Update velocity
        inertia = 0.5
        cognitive = 1.5 * np.random.random(dimensions) * (personal_best_positions[i] - particles[i])
        social = 1.5 * np.random.random(dimensions) * (global_best_position - particles[i])
        velocities[i] = inertia * velocities[i] + cognitive + social

        # Update position
        particles[i] += velocities[i]
        particles[i] = np.clip(particles[i], lower_bound, upper_bound)

        # Evaluate fitness
        fitness = pyramid_function(particles[i])
        if fitness < personal_best_scores[i]:
            personal_best_scores[i] = fitness
            personal_best_positions[i] = particles[i]
        if fitness < global_best_score:
            global_best_score = fitness
            global_best_position = particles[i]

    # Track global best score for this iteration
    iteration_costs.append(global_best_score)

# Print Results
print(f"The best position found is: {global_best_position}")
print(f"The best function value found is: {global_best_score}")

# Plot Convergence Over Iterations
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(iteration_costs) + 1), iteration_costs, marker="o", label="Cost")
plt.title("Convergence of PSO on Pyramid Function")
plt.xlabel("Iterations")
plt.ylabel("Cost")
plt.grid(True)
plt.legend()
plt.show()
