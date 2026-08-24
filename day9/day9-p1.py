import itertools

coordinates=[]
with open("inputs","r") as f:
    for line in f:
        parts = line.strip().split(",")
        coordinates.append((int(parts[0]),int(parts[1])))

    total_area = 0
    #itertools.combinations pairs up every point with every other point
    for coord_x,coord_y in itertools.combinations(coordinates,2):
        #unpack coords
        x1,y1 = coord_x
        x2,y2 = coord_y

        #abs makes sure all nrs are positive
        width = abs(x2-x1) + 1
        height = abs(y2-y1) + 1
        area = width*height
        #if next area is bigger overwrite it
        if area > total_area:
            total_area = area

print(total_area)

