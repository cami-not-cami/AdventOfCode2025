from collections import deque

#part 2 of day 10 works with the example inputs but hits a bottleneck
#when the specific inputs are put in
#i tried solving it with breadth first algorithm and things i found online from other solutions
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

def get_adjacent(current_state,button_list,target):
    neighbors = []
    for btn in button_list:
        next_state= list(current_state)
        valid=True
        for index in btn:
            next_state[index] += 1
            if next_state[index] > target[index]:
                valid = False
                break
        if valid:
            neighbors.append(tuple(next_state))
    return neighbors
def bfsConnected(button_wiring,target):
    start_state = tuple(0 for _ in target)

    q = deque()
    q.append((start_state,0))
    visited = set()
    visited.add(start_state)
    while q:
        current,presses = q.popleft()
        if current==target:
            return presses

        #visit all unvisited neighbours of current mode
        for adjacent in get_adjacent(current,button_wiring,target):
            if adjacent not in visited:
                visited.add(adjacent)
                q.append((adjacent,presses+1))
    return 0

#solves one row aka one machine
def solve_one(joltage_part, buttons_list):
    target = tuple(joltage_part)
    return bfsConnected(buttons_list,target)

total=0
for i in range(len(joltage)):
    res = solve_one(joltage[i],button_wiring[i])
    total += res

print(total)