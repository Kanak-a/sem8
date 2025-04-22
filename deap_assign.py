import random
from deap import base, creator, tools, algorithms

# Define the problem: Minimize Sphere function
def sphere(individual):
    return sum(x**2 for x in individual),  # comma makes it a tuple (DEAP expects this)

# Define individual and fitness
creator.create("FitnessMin", base.Fitness, weights=(-1.0,))  # minimize
creator.create("Individual", list, fitness=creator.FitnessMin)

toolbox = base.Toolbox()
# Attribute generator: random float between -5.0 and 5.0
toolbox.register("attr_float", random.uniform, -5.0, 5.0)

# Structure initializers
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=5)  # 5D solution
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

# Register the evaluation function and genetic operators
toolbox.register("evaluate", sphere)
toolbox.register("mate", tools.cxBlend, alpha=0.5)
toolbox.register("mutate", tools.mutGaussian, mu=0, sigma=1.0, indpb=0.2)
toolbox.register("select", tools.selTournament, tournsize=3)

# Run the algorithm
def main():
    pop = toolbox.population(n=50)
    hof = tools.HallOfFame(1)  # Store best solution
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("avg", lambda fits: round(sum(f[0] for f in fits) / len(fits), 4))
    stats.register("min", lambda fits: min(f[0] for f in fits))


    pop, log = algorithms.eaSimple(pop, toolbox,
                                   cxpb=0.7, mutpb=0.2,
                                   ngen=40, stats=stats,
                                   halloffame=hof, verbose=True)

    print("\nBest solution found:", hof[0])
    print("Fitness of best solution:", hof[0].fitness.values[0])

if __name__ == "__main__":
    main()
