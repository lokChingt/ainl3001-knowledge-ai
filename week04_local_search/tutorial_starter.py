"""
TU850-3
AINL3001 — Knowledge-Driven AI
Dr. Bianca Schoen-Phelan
2026

Week 4 Tutorial
Introducing the Problem Class

In previous weeks, we represented problems directly using
variables and functions.

From this week onwards, we will use a common Problem class
where appropriate.

This tutorial uses the familiar grid world from earlier weeks
to explore the new structure.
"""

from common.problem import Problem


GRID_SIZE = 5


class GridProblem(Problem):
    """
    A simple grid-world problem.

    A state is represented as an (x, y) coordinate.

    Example:

        (0, 0) = top-left corner
        (4, 4) = bottom-right corner
    """

    def actions(self, state):
        """
        Return the valid actions from this state.

        Possible actions:

            UP
            DOWN
            LEFT
            RIGHT

        Remember: an action must not move outside the grid.
        """

        # TODO:
        #
        # 1. Extract x and y from state.
        # 2. Create an empty list of actions.
        # 3. Check which movements are valid.
        # 4. Add valid actions to the list.
        # 5. Return the list.

        x, y = state
        actions = []

        action_dict = {
            "UP": (x - 1, y),
            "DOWN": (x + 1, y),
            "LEFT": (x, y - 1),
            "RIGHT": (x, y + 1)
        }

        for action, coord in action_dict.items():
            mx, my = coord

            inside_grid = (
                0 <= mx < GRID_SIZE and
                0 <= my < GRID_SIZE
            )

            if inside_grid:
                actions.append(action)

        return actions

    def result(self, state, action):
        """
        Return the new state produced by performing an action.

        Example:

            state  = (0, 0)
            action = "RIGHT"

            result = (1, 0)
        """

        # TODO:
        #
        # 1. Extract x and y from state.
        # 2. Check which action was requested.
        # 3. Return the resulting state.

        x, y = state

        action_dict = {
            "UP": (x - 1, y),
            "DOWN": (x + 1, y),
            "LEFT": (x, y - 1),
            "RIGHT": (x, y + 1)
        }

        return action_dict[action]


# --------------------------------------------------
# CREATE A PROBLEM
# --------------------------------------------------

problem = GridProblem(
    initial=(0, 0),
    goal=(4, 4)
)


# --------------------------------------------------
# EXPLORE THE PROBLEM
# --------------------------------------------------

print("Initial state:", problem.initial)
print("Goal:", problem.goal)


print("\nActions from (0, 0):")

actions = problem.actions((0, 0))

print(actions)


print("\nResults of those actions:")

if actions is not None:
    for action in actions:

        new_state = problem.result(
            (0, 0),
            action
        )

        print(
            action,
            "->",
            new_state
        )


print("\nIs (4, 4) the goal?")

print(
    problem.goal_test((4, 4))
)


# --------------------------------------------------
# REFLECTION QUESTIONS
# --------------------------------------------------

"""
Be ready to discuss:

1. What information is stored in problem.initial?

2. What information is stored in problem.goal?

3. What is the difference between:

       problem.actions(state)

   and:

       problem.result(state, action)

4. Why doesn't Problem know anything about grids?

5. Why doesn't GridProblem know anything about search?

6. Could the same Problem structure be used for something
   other than a grid?
"""