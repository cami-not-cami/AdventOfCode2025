with open("inputs") as f:
    grid = f.read().splitlines()
    #find where the beam starts
    start_col = grid[0].index('S')

    #keep track of which columns contain beams
    active_column = [start_col]
    total_split=0

    for row in grid:
        #array to keep track of where the next beams for the next rows will be
        next_cols = []
        for col in active_column:
            if row[col] == '^':
                total_split += 1
                #move the beam to new pos if we are splitting
                left_col= col-1
                right_col= col+1
                #add to next col if not already there
                if left_col not in next_cols:
                    next_cols.append(left_col)
                if right_col not in next_cols:
                    next_cols.append(right_col)
            else:
                #comtinue down
                if col not in next_cols:
                    next_cols.append(col)
        #reupdate the the cols with the ones i created
        active_column = next_cols
print(total_split)




