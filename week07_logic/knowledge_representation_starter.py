"""AINL3001 — Topic 7: Knowledge Representation and Logical Reasoning.

Student starter: complete the TODOs in Tasks 3 and 4.
This lab uses propositional facts and simple IF/THEN rules.

BSP
2026
"""

# TASK 1 — Represent facts (provided; inspect and experiment).
facts = {"rainy", "weekday"}

# TASK 2 — Represent rules (provided; inspect and experiment).
# Each rule is (list_of_required_facts, conclusion).
# All conditions must be known before the conclusion can be inferred.
rules = [
    (["rainy"], "take_umbrella"),
    (["rainy", "cold"], "wear_coat"),
    (["take_umbrella"], "stay_dry"),
]


def forward_chaining(known_facts, rules):
    """Return all original and inferred facts without changing known_facts.

    TASK 3 — TODO:
    1. Copy known_facts into a new set.
    2. Examine every rule and add its conclusion when ALL conditions hold.
    3. Repeat until an entire pass adds no new facts.
    4. Return the completed set.
    """
    # TODO
    
    inferred_facts = set(known_facts)

    for conditions, conclusion in rules:
        if all(condition in inferred_facts for condition in conditions):
            inferred_facts.add(conclusion)

    return inferred_facts


def query(inferred_facts, statement):
    """TASK 4 — Return True if statement is established in inferred_facts.

    A False result means 'not established', not necessarily 'false'.
    """
    # TODO

    return statement in inferred_facts


"""
TASK 5 — Backward chaining — TODO:
1. Which rule has stay_dry as its conclusion?           -- rule 3
2. What condition does that rule require?               -- take_umbrella
3. Which rule could establish that condition?           -- rainy
4. Does the chain ultimately reach an initial fact?     -- yes

Chain of Reasoning: rainy <- take_umbrella <- stay_dry
"""

"""
TASK 6 — Logic discussion — TODO:
Consider the rule `IF rainy THEN take_umbrella`.

Discuss:
1. Does this rule have to be true in the real world? -- no
2. What assumptions are we making when we include it in the knowledge base? -- if rainy, take umbrella
3. How is logical inference from an accepted rule different from statistical reasoning under uncertainty?
    -- Logical inference uses facts and rules, so if the condition is true, the statement is also true that everyone will take a umbrella. 
    -- Statistical reasoning uses prosibility and data, so it only know how much chance will people take umbrella when raining. 
        -- Doesn't guarantee everyone will take a umbrella in rainy days
"""


if __name__ == "__main__":
    print("=" * 55)
    print("TASK 0 — MANUAL REASONING")
    print("=" * 55)
    print("Initial facts:", sorted(facts))
    print("Rules:")
    for conditions, conclusion in rules:
        print(f"  IF {' AND '.join(conditions)} THEN {conclusion}")
    print("\nBefore coding, predict whether these can be inferred:")
    print("  take_umbrella?  stay_dry?  wear_coat?  Why?")
    print("  Ans: take_umbrella and stay_dry can be inferred because the condition exist, \n" \
    "       while we don't know whether it's cold or not so wear_coat cannot be inferred. ")

    print("\n" + "=" * 55)
    print("TASKS 3–4 — FORWARD CHAINING AND QUERIES")
    print("=" * 55)
    inferred = forward_chaining(facts, rules)
    if inferred is None:
        print("Complete forward_chaining() to see inferred knowledge.")
    else:
        print("Initial facts:", sorted(facts))
        print("All known facts:", sorted(inferred))
        for statement in ("take_umbrella", "stay_dry", "wear_coat"):
            print(f"Can infer {statement}? {query(inferred, statement)}")

    print("\nTASK 5 — BACKWARD CHAINING (discussion)")
    print("Goal: stay_dry. Which rule concludes it? What must be true first?")
    print("Ans: stay_dry concludes the take_umbrella rule, so rainy must be true first.")
    print("     Chain of Reasoning: rainy <- take_umbrella <- stay_dry")

    print("\nTASK 6 — LOGIC DISCUSSION")
    print("Is 'IF rainy THEN take_umbrella' always true in the real world?")
    print("What assumptions does the rule make?")
    print("Ans: It is not always true in the real world. It just assumes that everyone takes umbrella during rainy days")