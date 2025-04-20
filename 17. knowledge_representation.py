# Define facts and rules in logic

facts = {
    "man(marcus)",
    "pompeian(marcus)",
    "ruler(caesar)",
    "triedToAssassinate(marcus, caesar)"
}

rules = [
    # Rule: All pompeians are romans
    ("pompeian(X)", "roman(X)"),

    # All men are people
    ("man(X)", "person(X)"),

    # All romans are either loyal to Caesar or hate him
    ("roman(X)", "loyalto(X, caesar) or hates(X, caesar)"),

    # Everyone is loyal to someone
    ("person(X)", "exists(Y, loyalto(X, Y))"),

    # People only try to assassinate rulers they are not loyal to
    ("triedToAssassinate(X, Y) and ruler(Y) and not loyalto(X, Y)", "hates(X, Y)")
]

# We simulate inference manually

inferred = set(facts)

# Helper to check matching
def match_and_infer(rule, inferred_facts):
    premise, conclusion = rule
    new_facts = set()

    for var in ['marcus', 'caesar']:
        bound_premise = premise.replace("X", var).replace("Y", var)
        bound_conclusion = conclusion.replace("X", var).replace("Y", var)

        if "and" in bound_premise:
            parts = [p.strip() for p in bound_premise.split("and")]
            if all(p in inferred_facts for p in parts):
                if "or" in bound_conclusion:
                    # branching logic
                    for part in bound_conclusion.split("or"):
                        new_facts.add(part.strip())
                else:
                    new_facts.add(bound_conclusion)
        else:
            if bound_premise in inferred_facts:
                if "or" in bound_conclusion:
                    for part in bound_conclusion.split("or"):
                        new_facts.add(part.strip())
                else:
                    new_facts.add(bound_conclusion)

    return new_facts

# Inference loop
updated = True
while updated:
    updated = False
    for rule in rules:
        new = match_and_infer(rule, inferred)
        if not new.issubset(inferred):
            inferred.update(new)
            updated = True

# Final Answer
print("Inferred facts:")
for fact in inferred:
    print("-", fact)

# Check if Marcus hates Caesar
if "hates(marcus, caesar)" in inferred:
    print("\n✅ Answer: YES, Marcus hated Caesar.")
else:
    print("\n❌ Answer: Cannot infer hatred.")
