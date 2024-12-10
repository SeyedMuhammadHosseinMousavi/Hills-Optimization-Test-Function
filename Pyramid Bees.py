import numpy as np
import matplotlib.pyplot as plt

# Define the Pyramid Function
def pyramid_function(x):
    x = np.clip(np.array(x), -40.313, 40.313)  # Constrain variables
    term1 = np.sum(np.sin(x)) * 10  # Sinusoidal term
    term2 = np.sum(x ** 2) * 0.1    # Quadratic term for smoothness
    return term1 + term2

# Bees Algorithm Parameters
num_bees = 50  # Total number of bees
num_generations = 100  # Number of generations
elite_sites = 5  # Number of elite sites
elite_bees = 10  # Number of bees around elite sites
selected_sites = 10  # Number of selected sites (including elite sites)
selected_bees = 5  # Number of bees around selected sites
neighborhood_size = 1.0  # Neighborhood size for local search
dimensions = 6
lower_bound = -40.313
upper_bound = 40.313

# Initialize population
population = np.random.uniform(low=lower_bound, high=upper_bound, size=(num_bees, dimensions))
fitness = np.array([pyramid_function(ind) for ind in population])

# Store best fitness values for convergence plot
best_fitness_per_generation = []

# Main Bees Algorithm
for generation in range(num_generations):
    # Sort the population by fitness
    sorted_indices = np.argsort(fitness)
    population = population[sorted_indices]
    fitness = fitness[sorted_indices]

    # Best solution is at the top
    best_solution = population[0]
    best_fitness = fitness[0]

    # Store the best fitness of the generation
    best_fitness_per_generation.append(best_fitness)

    # Generate new solutions
    new_population = []

    # Elite sites
    for i in range(elite_sites):
        for _ in range(elite_bees):
            neighbor = population[i] + np.random.uniform(-neighborhood_size, neighborhood_size, dimensions)
            neighbor = np.clip(neighbor, lower_bound, upper_bound)
            new_population.append(neighbor)

    # Selected sites (excluding elite sites)
    for i in range(elite_sites, selected_sites):
        for _ in range(selected_bees):
            neighbor = population[i] + np.random.uniform(-neighborhood_size, neighborhood_size, dimensions)
            neighbor = np.clip(neighbor, lower_bound, upper_bound)
            new_population.append(neighbor)

    # Remaining bees explore randomly
    while len(new_population) < num_bees:
        random_solution = np.random.uniform(low=lower_bound, high=upper_bound, size=dimensions)
        new_population.append(random_solution)

    # Evaluate fitness of the new population
    new_population = np.array(new_population)
    fitness = np.array([pyramid_function(ind) for ind in new_population])

    # Update the population
    population = new_population

# Print Results
print(f"The best solution found is: {best_solution}")
print(f"The best function value found is: {best_fitness}")

# Plot Convergence Over Generations
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(best_fitness_per_generation) + 1), best_fitness_per_generation, marker="o", label="Cost")
plt.title("Convergence of Bees Algorithm Pyramid Function (Cost Minimization)")
plt.xlabel("Generations")
plt.ylabel("Cost")
plt.grid(True)
plt.legend()
plt.show()
