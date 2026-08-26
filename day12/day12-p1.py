with open('inputs') as f:
    input_text = f.read()

    #separate shape definitions section from the region specifications section
    sections = input_text.strip().split("\n\n")
    #extracts just the shape definitions
    shape_sections = sections[:-1]
    #the block of text containing all the tree regions
    region_lines = sections[-1].strip().split("\n")

    # calculate area (count of '#') for each shape index
    shape_areas = [shape.count('#') for shape in shape_sections]
    print(shape_areas)
    valid_regions_count = 0

    for line in region_lines:
        dimensions, counts = line.split(": ")
        w, h = map(int, dimensions.split("x"))
        available_area = w * h

        #turns the nr inputs from string to a list of ints
        #quantity of each shape
        qty_list = list(map(int, counts.split()))

        shape_totals = []
        # multiply each shape's quantity by its area and store the results
        for qty, area in zip(qty_list, shape_areas):
            shape_totals.append(qty * area)
        # sum the total area needed by all requested presents
        required_area = sum(shape_totals)
        # check if required area fits
        if required_area <= available_area:
            valid_regions_count += 1


print(valid_regions_count)

