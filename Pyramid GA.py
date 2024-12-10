import numpy as np
import matplotlib.pyplot as plt
from deap import base, creator, tools, algorithms

# Define the Pyramid Function
def pyramid_function(individual):
    x = np.clip(np.array(individual), -40.313, 40.313)  # Constrain variables
    term1 = np.sum(np.sin(x)) * 10  # Sinusoidal term
    term2 = np.sum(x ** 2) * 0.1    # Quadratic term for smoothness
    return term1 + term2,  # Return as a tuple for DEAP compatibility

# GA Parameters
num_individuals = 50  # Population size
num_generations = 100
dimensions = 6
mutation_rate = 0.2
crossover_rate = 0.5
lower_bound = -40.313
upper_bound = 40.313

# DEAP Setup
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # Minimize the fitness
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, lower_bound, upper_bound)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, dimensions)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", pyramid_function)
toolbox.register("mate", tools.cxBlend, alpha=0.5)  # Blend crossover
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1, indpb=0.2)  # Gaussian mutation
toolbox.register("select", tools.selTournament, tournsize=3)  # Tournament selection

# Initialize Population
population = toolbox.population(n=num_individuals)

# Store best fitness values for plotting
logbook = tools.Logbook()
logbook.header = ["gen", "min", "avg", "max"]

# GA Execution
stats = tools.Statistics(lambda ind: ind.fitness.values)
stats.register("min", np.min)
stats.register("avg", np.mean)
stats.register("max", np.max)

population, log = algorithms.eaSimple(population, toolbox, cxpb=crossover_rate, mutpb=mutation_rate,
                                       ngen=num_generations, stats=stats, verbose=True)

# Extract the best individual and its fitness
best_individual = tools.selBest(population, k=1)[0]
best_fitness = pyramid_function(best_individual)[0]

# Print Results
print(f"The best individual found is: {best_individual}")
print(f"The best function value found is: {best_fitness}")

# Plot Convergence Over Generations
generations = log.select("gen")
min_fitness = log.select("min")

plt.figure(figsize=(10, 6))
plt.plot(generations, min_fitness, marker="o", label="Min Fitness")
plt.title("Convergence of GA on Pyramid Function (Cost Minimization)")
plt.xlabel("Generations")
plt.ylabel("Cost")
plt.grid(True)
plt.legend()
plt.show()
