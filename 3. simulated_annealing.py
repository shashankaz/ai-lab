import math
import random

def distance(path, graph):
    return sum(graph[path[i]][path[(i + 1) % len(path)]] for i in range(len(path)))

def simulated_annealing(graph, initial_temp=10000, cooling_rate=0.995, stop_temp=1e-8, max_iter=1000):
    n = len(graph)
    # Initial random solution
    current_path = list(range(n))
    random.shuffle(current_path)
    current_cost = distance(current_path, graph)

    best_path = list(current_path)
    best_cost = current_cost

    temp = initial_temp
    iteration = 0

    while temp > stop_temp and iteration < max_iter:
        # Swap two cities to create a new neighbor
        new_path = list(current_path)
        i, j = random.sample(range(n), 2)
        new_path[i], new_path[j] = new_path[j], new_path[i]

        new_cost = distance(new_path, graph)
        delta = new_cost - current_cost

        # Accept new solution with probability
        if delta < 0 or random.random() < math.exp(-delta / temp):
            current_path = new_path
            current_cost = new_cost
            if current_cost < best_cost:
                best_path = list(current_path)
                best_cost = current_cost

        temp *= cooling_rate
        iteration += 1

    return best_path, best_cost

# Example graph (symmetric TSP)
graph = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

path, cost = simulated_annealing(graph)
print("Best path found:", path)
print("Total cost:", cost)
