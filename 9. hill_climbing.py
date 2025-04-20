import random

def hill_climbing(func, x_start, max_iterations=1000, step_size=0.1):
    current_x = x_start
    current_value = func(current_x)

    for _ in range(max_iterations):
        # Explore neighbors
        next_x = current_x + random.choice([-step_size, step_size])
        next_value = func(next_x)

        # Move if the neighbor is better
        if next_value > current_value:
            current_x, current_value = next_x, next_value
        else:
            # No better neighbor, stop
            break

    return current_x, current_value

# Objective function
def objective_function(x):
    return -x**2 + 10*x

# Run the algorithm
best_x, best_val = hill_climbing(objective_function, x_start=random.uniform(0, 10))
print(f"Best x: {best_x:.4f}")
print(f"Maximum value: {best_val:.4f}")
