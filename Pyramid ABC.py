import numpy as np
import matplotlib.pyplot as plt

# Define the Pyramid Function
def pyramid_function(x):
    x = np.clip(np.array(x), -40.313, 40.313)  # Constrain variables
    term1 = np.sum(np.sin(x)) * 10  # Sinusoidal term
    term2 = np.sum(x ** 2) * 0.1    # Quadratic term for smoothness
    return term1 + term2

# ABC Parameters
num_bees = 50  # Number of bees in the colony
num_generations = 100  # Maximum iterations
dimensions = 6
lower_bound = -40.313
upper_bound = 40.313
limit = 10  # Limit for abandoning a food source

# Initialize bees (food sources)
population = np.random.uniform(low=lower_bound, high=upper_bound, size=(num_bees, dimensions))
fitness = np.array([pyramid_function(ind) for ind in population])  # Evaluate initial fitness
trials = np.zeros(num_bees)  # Trial counter for each bee

# Store best fitness values for plotting
best_fitness_per_generation = []

# Main ABC Algorithm
for generation in range(num_generations):
    # EMPLOYED BEES PHASE
    for i in range(num_bees):
        # Generate a new solution for the i-th bee
        phi = np.random.uniform(-1, 1, dimensions)  # Random direction
        k = np.random.choice([idx for idx in range(num_bees) if idx != i])  # Random other bee
        new_solution = population[i] + phi * (population[i] - population[k])
        new_solution = np.clip(new_solution, lower_bound, upper_bound)  # Ensure bounds

        # Evaluate new fitness
        new_fitness = pyramid_function(new_solution)
        if new_fitness < fitness[i]:  # Minimization problem
            population[i] = new_solution
            fitness[i] = new_fitness
            trials[i] = 0  # Reset trial counter
        else:
            trials[i] += 1  # Increment trial counter

    # ONLOOKER BEES PHASE
    fitness_prob = np.maximum(1 / (fitness + 1e-10), 0)  # Higher probability for better fitness
    fitness_prob /= np.sum(fitness_prob)  # Normalize probabilities
    for _ in range(num_bees):
        i = np.random.choice(range(num_bees), p=fitness_prob)
        phi = np.random.uniform(-1, 1, dimensions)  # Random direction
        k = np.random.choice([idx for idx in range(num_bees) if idx != i])  # Random other bee
        new_solution = population[i] + phi * (population[i] - population[k])
        new_solution = np.clip(new_solution, lower_bound, upper_bound)  # Ensure bounds

        # Evaluate new fitness
        new_fitness = pyramid_function(new_solution)
        if new_fitness < fitness[i]:
            population[i] = new_solution
            fitness[i] = new_fitness
            trials[i] = 0  # Reset trial counter
        else:
            trials[i] += 1  # Increment trial counter

    # SCOUT BEES PHASE
    for i in range(num_bees):
        if trials[i] > limit:  # Abandon food source
            population[i] = np.random.uniform(low=lower_bound, high=upper_bound, size=dimensions)
            fitness[i] = pyramid_function(population[i])
            trials[i] = 0  # Reset trial counter

    # Store the best fitness of the current generation
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
plt.title("Convergence of ABC Pyramid Function (Cost Minimization)")
plt.xlabel("Generations")
plt.ylabel("Cost")
plt.grid(True)
plt.legend()
plt.show()
