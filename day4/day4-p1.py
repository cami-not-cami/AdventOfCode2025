#this is like minesweeper except instead of bombs i check for rolls next to my roll
with open("inputs") as f:
    grid = [line.strip() for line in f if line.strip()]

    #separate in rows and cols
    rows = len(grid)
    cols = len(grid[0])

directions = [
    (-1, -1), (-1, 0), (-1, 1),
    ( 0, -1),( 0, 1),
    ( 1, -1), ( 1, 0), ( 1, 1)
]
accessible_rolls=0

for row in range(rows):
    for col in range(cols):
        #if it is a roll
        if grid[row][col] == "@":
            #reset neighbour
            neighbour=0
            for x, y in directions:
                neighbour_row  = row + x
                neighbour_col = col + y
                #checking for rolls in perimeter with the relative coords
                if 0 <= neighbour_row < rows and 0 <= neighbour_col < cols:
                    if grid[neighbour_row][neighbour_col] == "@":
                        neighbour+=1
            #if there are fewer than four rolls of paper in the eight adjacent positions
            #then we can count it as accessible
            if neighbour < 4:
                accessible_rolls+=1

print(accessible_rolls)




