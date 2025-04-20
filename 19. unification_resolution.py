def unify(x, y, subs={}):
    if subs is None:
        return None
    elif x == y:
        return subs
    elif isinstance(x, str) and x.islower():
        return unify_var(x, y, subs)
    elif isinstance(y, str) and y.islower():
        return unify_var(y, x, subs)
    elif isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            subs = unify(a, b, subs)
        return subs
    else:
        return None

def unify_var(var, x, subs):
    if var in subs:
        return unify(subs[var], x, subs)
    elif x in subs:
        return unify(var, subs[x], subs)
    else:
        subs[var] = x
        return subs

def resolve(facts, goal):
    for fact in facts:
        subs = unify(fact, goal, {})
        if subs is not None:
            return True, subs
    return False, None

# Knowledge base (facts)
facts = [
    ('father', 'john', 'bob'),
    ('father', 'bob', 'mike')
]

# Rule: father(X, Y) ∧ father(Y, Z) → grandfather(X, Z)
def infer_grandfather(facts):
    for f1 in facts:
        if f1[0] == 'father':
            x, y = f1[1], f1[2]
            for f2 in facts:
                if f2[0] == 'father' and f2[1] == y:
                    z = f2[2]
                    return ('grandfather', x, z)
    return None

# Goal we want to prove
goal = ('grandfather', 'john', 'mike')

# Inference process
derived_fact = infer_grandfather(facts)
found, subs = resolve([derived_fact], goal)

print("Knowledge Base:")
for f in facts:
    print(f"  {f[0]}({f[1]}, {f[2]})")

print("\nTrying to prove:", f"{goal[0]}({goal[1]}, {goal[2]})")

if found:
    print("✅ Result: Goal proved by resolution.")
    print("Derived substitution:", subs)
else:
    print("❌ Result: Could not prove the goal.")
