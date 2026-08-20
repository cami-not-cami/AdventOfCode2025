with open("inputs") as f:
    grid = f.read().splitlines()
    #find where the beam starts
    start_col = grid[0].index('S')

    #set that gets updated with the column and how many times a timeline goes threre like 3:1
    active_column = {start_col:1}


    for row in grid:
        #set to keep track of where the next beams for the next rows will be
        next_cols = {}
        for col,count in active_column.items():
            if row[col] == '^':
                #splits the beams to the left and right of the splitter
                #increases the count of occurences
               next_cols[col-1]= next_cols.get(col-1,0)+count
               next_cols[col+1]= next_cols.get(col+1,0)+count
            else:
                #add the rest which are not splitters
                next_cols[col]= next_cols.get(col,0)+count
        #reupdate the the cols with the ones that got created
        active_column = next_cols
#sums up all the values in the set
print(sum(active_column.values()))




