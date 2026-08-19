# same concept but remove accesible rolls then recheck which are accessible
with open("inputs") as f:
    grid = [list(line.strip()) for line in f if line.strip()]
    # separate in rows and cols
    rows = len(grid)
    cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    (0, -1), (0, 1),
    (1, -1), (1, 0), (1, 1)
]
total_removed = 0
while True:
    to_remove = []

    for row in range(rows):
        for col in range(cols):
            # if it is a roll
            if grid[row][col] == "@":
                # reset neighbour
                neighbour = 0
                for x, y in directions:
                    neighbour_row = row + x
                    neighbour_col = col + y
                    # checking for rolls in perimeter with the relative coords
                    if 0 <= neighbour_row < rows and 0 <= neighbour_col < cols:
                        if grid[neighbour_row][neighbour_col] == "@":
                            neighbour += 1
                            grid[row][col] = "@"

                # if there are fewer than four rolls of paper in the eight adjacent positions
                # then we can count it as accessible so remove it
                if neighbour < 4:
                    to_remove.append((row, col))

    #stop the loop
    if not to_remove:
        break
    for row, col in to_remove:
        grid[row][col] = "."

    total_removed += len(to_remove)

print("Total rolls removed:", total_removed)
