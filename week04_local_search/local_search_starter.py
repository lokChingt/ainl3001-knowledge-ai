"""
AINL3001 — Knowledge-Driven AI
Week 4 — Local Search and Optimisation
BSP 2026

This week introduces local search.

In previous weeks, search algorithms explored paths through
a state space in order to reach a goal.

Local search takes a different approach:

    1. Start with a state.
    2. Evaluate how good that state is.
    3. Generate neighbouring states.
    4. Move to a better neighbour.
    5. Repeat.

We will explore this using the N-Queens problem.

Tasks
-----

1. Understand the problem representation.
2. Implement conflict counting.
3. Explore neighbouring states.
4. Implement Hill Climbing.
5. Implement Simulated Annealing.
"""

import math
import random

from queens_problem import QueensProblem

N = 8


# --------------------------------------------------
# TASK 0 — UNDERSTANDING THE STATE
# --------------------------------------------------

example_board = [0, 1, 2, 3]

print("Manual Exploration Board:")
print(example_board)

print(
    "\nEach list position represents a column."
)

print(
    "Each value represents the row containing the queen."
)

print(
    "\nQuestion: How many conflicts exist on this board?"
)


# --------------------------------------------------
# TASK 1 — EVALUATE A STATE
# --------------------------------------------------

def count_conflicts(board):
    """
    Return the number of pairs of queens
    that attack each other.

    Lower values are better.

    A solution has:

        conflict count = 0
    """

    # TODO:
    # Compare each queen with every queen
    # that comes after it.
    #
    # Queens conflict when they are:
    #
    #   1. in the same row
    #   2. on the same diagonal

    n = len(board)
    count = 0

    for i in range(n):
        for j in range(i + 1, n):
            x1, y1 = i, board[i]
            x2, y2 = j, board[j]

            same_row = y1 == y2
            same_diagonal = abs(x2 - x1) == abs(y2 - y1)

            if same_row or same_diagonal:
                count += 1

    return count

# --------------------------------------------------
# TASK 2 — EXPLORE THE PROBLEM
# --------------------------------------------------

def generate_neighbours(problem, board):
    """
    Generate all neighbouring boards.

    Use the Problem interface introduced this week:

        problem.actions(state)
        problem.result(state, action)
    """

    neighbours = []

    # TODO:
    #
    # 1. Ask the problem for the available actions.
    # 2. Apply each action.
    # 3. Add the resulting state to neighbours.

    actions = problem.actions(board)

    for action in actions:
        new_state = problem.result(board, action)
        neighbours.append(new_state)

    return neighbours


# --------------------------------------------------
# TASK 3 — HILL CLIMBING
# --------------------------------------------------

def hill_climbing(problem, start_board):
    """
    Use Hill Climbing to reduce the number
    of conflicts.

    Algorithm:

        current = start state

        repeat:

            generate neighbours

            find the neighbour with the
            lowest conflict count

            if the neighbour is not better:
                stop

            otherwise:
                move to the neighbour

        return current
    """

    def lowest_conflicts(neighbours):
        min_conflicts = 100
        lowest_conflicts_neighbour = []

        for neighbour in neighbours:
            curr_conflicts = count_conflicts(neighbour)

            if curr_conflicts < min_conflicts:
                min_conflicts = curr_conflicts
                lowest_conflicts_neighbour = neighbour

        #print("lowest_conflicts_neighbour:", lowest_conflicts_neighbour)
        #print("min_conflicts", min_conflicts)

        return lowest_conflicts_neighbour, min_conflicts


    current = start_board

    min_conflicts = count_conflicts(current)

    while min_conflicts > 0:
        neighbours = generate_neighbours(
            problem,
            current
        )

        current, min_conflicts = lowest_conflicts(neighbours)

    return current


# --------------------------------------------------
# TASK 4 — SIMULATED ANNEALING
# --------------------------------------------------

def simulated_annealing(problem, start_board):
    """
    Use Simulated Annealing to search for
    a solution.

    Unlike Hill Climbing, Simulated Annealing
    can sometimes accept a worse state.

    This can help escape local minima.
    """

    current = start_board

    temperature = 10.0
    cooling_rate = 0.95

    # TODO

    while temperature > 0.01:
        actions = problem.actions(current)

        random_action = random.choice(actions)
        random_neighbour = problem.result(current, random_action)

        delta_e = count_conflicts(current) - count_conflicts(random_neighbour)
        #print("random_neighbour", random_neighbour)
        #print("conflicts", count_conflicts(random_neighbour))

        if delta_e > 0:
            current = random_neighbour
        else:
            accept_prob = math.exp(delta_e / temperature)

            if accept_prob > random.random():
                current = random_neighbour

        temperature *= cooling_rate

    return current


# --------------------------------------------------
# TESTING AREA
# --------------------------------------------------

if __name__ == "__main__":

    board = [
        random.randint(0, N - 1)
        for _ in range(N)
    ]

    problem = QueensProblem(board)

    print("\nRandom Board")
    print(board)

    print("\nConflicts")
    print(
        count_conflicts(board)
    )

    print("\nPossible Actions")
    
    actions = problem.actions(board)

    print(
        f"{len(actions)} actions available"
    )

    print("\nNeighbours")

    neighbours = generate_neighbours(
        problem,
        board
    )

    print(
        f"{len(neighbours)} neighbours generated"
    )


    print("\nHill Climbing:")
    current = hill_climbing(problem, board)
    print(current)
    print("conflicts:", count_conflicts(current))


    print("\nSimulated Annealing:")
    current = simulated_annealing(problem, board)
    print(current)
    print("conflicts:", count_conflicts(current))