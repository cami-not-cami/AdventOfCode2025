#solved with ai, i dont know linear algebra and i just wanted my star
import os
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds


def solve_machine_scipy(joltage_target, button_list):
    n_buttons = len(button_list)
    n_counters = len(joltage_target)

    # Coefficient matrix A: A[i, j] = 1 if counter i in button j
    A = np.zeros((n_counters, n_buttons))
    for j, btn in enumerate(button_list):
        for i in btn:
            A[i, j] = 1

    c = np.ones(n_buttons)  # Objective: minimize sum(x_j)
    constraints = LinearConstraint(A, joltage_target, joltage_target)
    integrality = np.ones(n_buttons)  # All integer variables
    bounds = Bounds(0, np.inf)

    res = milp(c=c, integrality=integrality, constraints=constraints, bounds=bounds)
    if res.success:
        return int(np.round(res.fun))
    return 0


def main():
    button_wiring = []
    joltage = []

    input_path = os.path.join(os.path.dirname(__file__), "inputs")
    with open(input_path, "r") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue

            diagram_part, rest = line.split("]", 1)
            wiring_part, joltage_part = rest.split("{", 1)

            j_nums = [
                int(x)
                for x in joltage_part.replace("}", "").split(",")
                if x.strip()
            ]

            buttons = []
            for group in wiring_part.split("("):
                cleaned = group.replace(")", "").strip()
                if cleaned:
                    buttons.append([int(x) for x in cleaned.split(",") if x.strip()])

            button_wiring.append(buttons)
            joltage.append(j_nums)

    total = 0
    for i in range(len(joltage)):
        res = solve_machine_scipy(joltage[i], button_wiring[i])
        total += res

    print("Total minimum button presses:", total)


if __name__ == "__main__":
    main()
