import numpy as np
import matplotlib.pyplot as plt

# Define the Pyramid Function
def pyramid_function(x):
    x = np.clip(np.array(x), -40.313, 40.313)  # Constrain variables
    term1 = np.sum(np.sin(x)) * 10  # Sinusoidal term
    term2 = np.sum(x ** 2) * 0.1    # Quadratic term for smoothness
    return term1 + term2

# DE Parameters
num_individuals = 50  # Population size
num_generations = 100  # Number of generations
dimensions = 6
lower_bound = -40.313
upper_bound = 40.313
mutation_factor = 0.8  # Mutation factor (F)
crossover_probability = 0.7  # Crossover probability (CR)

# Initialize population
population = np.random.uniform(low=lower_bound, high=upper_bound, size=(num_individuals, dimensions))

# Evaluate initial fitness
fitness = np.array([pyramid_function(ind) for ind in population])

# Store best fitness values for convergence plot
best_fitness_per_generation = []

# Main DE Algorithm
for generation in range(num_generations):
    new_population = []
    for i in range(num_individuals):
        # Mutation: Select three random individuals (not including the current one)
        indices = [idx for idx in range(num_individuals) if idx != i]
        a, b, c = population[np.random.choice(indices, 3, replace=False)]

        # Generate mutant vector
        mutant = a + mutation_factor * (b - c)
        mutant = np.clip(mutant, lower_bound, upper_bound)  # Ensure bounds

        # Crossover: Create trial vector
        trial = np.array([mutant[j] if np.random.rand() < crossover_probability else population[i][j]
                          for j in range(dimensions)])

        # Selection: Compare trial vector with current individual
        trial_fitness = pyramid_function(trial)
        if trial_fitness < fitness[i]:  # Minimization problem
            new_population.append(trial)
            fitness[i] = trial_fitness
        else:
            new_population.append(population[i])

    # Update population
    population = np.array(new_population)

    # Track the best fitness in the current generation
    best_fitness_per_generation.append(np.min(fitness))

# Extract the best solution
best_index = np.argmin(fitness)
best_solution = population[best_index]
best_fitness = fitness[best_index]

# Print Results
print(f"The best solution found is: {best_solution}")
print(f"The best function value found is: {best_fitness}")

# Plot Convergence Over Generations
plt.figure(figsize=(10, 6))
plt.plot(range(1, len(best_fitness_per_generation) + 1), best_fitness_per_generation, marker="o", label="Cost")
plt.title("Convergence of DE on Pyramid Function (Cost Minimization)")
plt.xlabel("Generations")
plt.ylabel("Cost")
plt.grid(True)
plt.legend()
plt.show()
