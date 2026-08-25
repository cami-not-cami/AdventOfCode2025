import os
import numpy as np
from scipy.optimize import milp, LinearConstraint, Bounds
from collections import deque

#part 2 of day 10 works with the example inputs but hits a bottleneck
#when the specific inputs are put in
#i tried solving it with breadth first algorithm and things i found online from other solutions
#the working part is made with ai, i dont know how i could improve performance my way/ i dont understand linear integer algebra in python
light_diagramm = []
button_wiring = []
joltage = []


with open("inputs", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        diagram_part, rest = line.split("]", 1)
        diagram = diagram_part.replace("[", "").strip()

        wiring_part, joltage_part = rest.split("{", 1)

        # parse numbers, clear } and split on commas
        j_nums = [
            int(x)
            for x in joltage_part.replace("}", "").split(",")
            if x.strip()
        ]

        #split on ( to isolate each buttons
        buttons = []
        for group in wiring_part.split("("):
            cleaned = group.replace(")", "").strip()
            if cleaned:
                buttons.append([int(x) for x in cleaned.split(",") if x.strip()])

        light_diagramm.append(diagram)
        button_wiring.append(buttons)
        joltage.append(j_nums)


#solved with ai, i dont know linear algebra and i just wanted my star

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



#only works with example inputs, the huge inputs bottleneck it
# def get_adjacent(current_state,button_list,target):
#     neighbors = []
#     for btn in button_list:
#         next_state= list(current_state)
#         valid=True
#         for index in btn:
#             next_state[index] += 1
#             if next_state[index] > target[index]:
#                 valid = False
#                 break
#         if valid:
#             neighbors.append(tuple(next_state))
#     return neighbors
# def bfsConnected(button_wiring,target):
#     start_state = tuple(0 for _ in target)
#
#     q = deque()
#     q.append((start_state,0))
#     visited = set()
#     visited.add(start_state)
#     while q:
#         current,presses = q.popleft()
#         if current==target:
#             return presses
#
#         #visit all unvisited neighbours of current mode
#         for adjacent in get_adjacent(current,button_wiring,target):
#             if adjacent not in visited:
#                 visited.add(adjacent)
#                 q.append((adjacent,presses+1))
#     return 0
#
# #solves one row aka one machine
# def solve_one(joltage_part, buttons_list):
#     target = tuple(joltage_part)
#     return bfsConnected(buttons_list,target)
#
# total=0
# for i in range(len(joltage)):
#     res = solve_one(joltage[i],button_wiring[i])
#     total += res
#
# print(total)