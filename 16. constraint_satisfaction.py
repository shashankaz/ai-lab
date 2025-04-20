# Define CSP
variables = ['WA', 'NT', 'SA', 'Q', 'NSW', 'V', 'T']
domains = {var: ['Red', 'Green', 'Blue'] for var in variables}

neighbors = {
    'WA': ['NT', 'SA'],
    'NT': ['WA', 'SA', 'Q'],
    'SA': ['WA', 'NT', 'Q', 'NSW', 'V'],
    'Q': ['NT', 'SA', 'NSW'],
    'NSW': ['SA', 'Q', 'V'],
    'V': ['SA', 'NSW'],
    'T': []
}

def is_consistent(var, value, assignment):
    for neighbor in neighbors[var]:
        if neighbor in assignment and assignment[neighbor] == value:
            return False
    return True

def backtrack(assignment):
    if len(assignment) == len(variables):
        return assignment

    unassigned = [v for v in variables if v not in assignment]
    var = unassigned[0]

    for value in domains[var]:
        if is_consistent(var, value, assignment):
            assignment[var] = value
            result = backtrack(assignment)
            if result:
                return result
            del assignment[var]
    return None

# Solve CSP
solution = backtrack({})
print("Solution:", solution)
