ranges = []
numbers = []

with open("inputs", "r") as file:
    for line in file:
        line = line.strip()
        if not line:
            continue  # skip empty lines
        if "-" in line:
            start, end = map(int, line.split("-"))
            ranges.append((start, end))
        else:
            numbers.append(int(line))

in_range = [
    num for num in numbers
    if any(start <= num <= end for start, end in ranges)
]
total_fresh = len(in_range)

print("Numbers in range:", total_fresh)
#print("Ranges:", ranges)
#print("Numbers:", numbers)