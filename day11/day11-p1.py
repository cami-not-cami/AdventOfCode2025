graph = {} #dictionary key-value pairs
with open("inputs", "r") as f:
    for line in f:
        line = line.strip()

        device_part, outputs_part = line.split(":", 1)
        device = device_part.strip()
        outputs = outputs_part.strip().split()

        graph[device] = outputs

def count_paths(current_state, target):
    if current_state == target:
        return 1

    total_paths = 0
    for adjacent in graph.get(current_state, []):
        total_paths += count_paths(adjacent, target)

    return total_paths

# calculate total of paths
total = count_paths("you", "out")
print(total)