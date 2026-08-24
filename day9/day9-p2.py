import itertools

#read input coordinates (red tiles)
coordinates = []
with open("inputs", "r") as f:
    for line in f:
        parts = line.strip().split(",")
        coordinates.append((int(parts[0]), int(parts[1])))

# build line segments connecting consecutive points
horizontal_lines = []
vertical_lines = []

n = len(coordinates)
for i in range(n):
    point1 = coordinates[i]  # Current point
    # connect to next point; (i + 1) % n wraps back to index 0 at the end
    point2 = coordinates[(i + 1) % n]
    
    if point1[1] == point2[1]:  #if they have the same y coord (horizontal line)
        horizontal_lines.append((point1[1], min(point1[0], point2[0]), max(point1[0], point2[0])))
    else:  # if they have the same x coord (vertical line)
        vertical_lines.append((point1[0], min(point1[1], point2[1]), max(point1[1], point2[1])))

# check if a point (point_x, point_y) is inside or on the boundary
def is_inside(point_x, point_y):
    #check if point lies directly on any horizontal line
    for y, min_x, max_x in horizontal_lines:
        if point_y == y and min_x <= point_x <= max_x:
            return True
            
    #check if point lies directly on any vertical line
    for x, min_y, max_y in vertical_lines:
        if point_x == x and min_y <= point_y <= max_y:
            return True

    # ray casting: count how many vertical walls are to the right of the point
    intersections = 0
    for x, min_y, max_y in vertical_lines:
        if x > point_x and min_y <= point_y < max_y:
            intersections += 1
            
    # odd number of wall crossings (% 2 == 1) means INSIDE the bounds
    return intersections % 2 == 1


total_area = 0

# try every pair of points as opposite corners of a rectangle
for coord_x, coord_y in itertools.combinations(coordinates, 2):
    x1, y1 = coord_x
    x2, y2 = coord_y

    width = abs(x2 - x1) + 1
    height = abs(y2 - y1) + 1
    area = width * height

    #only check validation if this area is larger than our best so far
    if area > total_area:
        min_x, max_x = min(x1, x2), max(x1, x2)
        min_y, max_y = min(y1, y2), max(y1, y2)
        valid = True

        # does any horizontal fence line slice through the rectangle?
        for y, lx, rx in horizontal_lines:
            if min_y < y < max_y and max(lx, min_x) < min(rx, max_x):
                valid = False
                break

        # does any vertical fence line slice through the rectangle?
        if valid:
            for x, ly, ry in vertical_lines:
                if min_x < x < max_x and max(ly, min_y) < min(ry, max_y):
                    valid = False
                    break

        # is the center point of the rectangle inside the bounds?
        if valid:
            mid_x = (x1 + x2) / 2
            mid_y = (y1 + y2) / 2
            if not is_inside(mid_x, mid_y):
                valid = False

        # replace with largest area
        if valid:
            total_area = area

print(total_area)