ranges = []

with open("inputs", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))

## My way
# it sadly would take a long time to work with the bunch of ranges i have
#does work with small ranges/ less stuff to calculate
#
# min_val = min(start for start, end in ranges)
# max_val = max(end for start, end in ranges)
#
# total_fresh = sum(
#     1
#     for num in range(min_val, max_val + 1)
#     if any(start <= num <= end for start, end in ranges)
# )
#
# print("Total fresh IDs:", total_fresh)

## Improvement with help of AI for performance-
# sort ranges by their start bound
ranges.sort(key=lambda r: r[0])

# merge overlapping or touching ranges so i dont run useless calculations
merged = []
for start, end in ranges:
    if merged and start <= merged[-1][1] + 1:
        merged[-1][1] = max(merged[-1][1], end)
    else:
        merged.append([start, end])

# calculate total fresh IDs  using math
#basically total count using math: (end - start + 1)
#it is accurate because we already sorted and merged the id can only show up once
total_fresh = sum(end - start + 1 for start, end in merged)

print("Total fresh IDs:", total_fresh)