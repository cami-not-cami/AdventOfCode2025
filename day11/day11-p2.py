#with assitance from ai, i didnt know what dfs is before
#but now i do! :D
graph = {}

# Parse input file into a dict with key value pairs
#device is the key output is the value
with open("inputs", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue
        device, outputs = line.split(":", 1)
        graph[device.strip()] = outputs.strip().split()

# Memoized function to count paths from  start_node to  end_node
#a memoized function is a memory optimised function
#Memoization is a computer optimization technique that stores the results of expensive function calls.
#caches a response so it doesnt calculate it twice for eg
def count_paths(start_node, end_node):
    memo = {}
    #depth first search algorithm
    #it starts at a target node and follows one chain of device connections continuously until it hits a dead end or reaches the end_node
    #in my case it will check certain orders
    def dfs(curr):
        if curr == end_node:
            return 1
        if curr in memo:
            return memo[curr]

        total = 0
        for adjacent in graph.get(curr, []):
            total += dfs(adjacent)

        memo[curr] = total
        return total

    return dfs(start_node)

# svr -> dac -> fft -> out
paths_dac_first = (
    count_paths("svr", "dac") *
    count_paths("dac", "fft") *
    count_paths("fft", "out")
)
# svr -> fft -> dac -> out
paths_fft_first = (
    count_paths("svr", "fft") *
    count_paths("fft", "dac") *
    count_paths("dac", "out")
)

# total visiting both
total_paths = paths_dac_first + paths_fft_first

print({total_paths})