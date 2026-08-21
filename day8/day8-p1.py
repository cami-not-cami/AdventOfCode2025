#sqrt((x2 − x1)^2 + (y2 − y1)^2) - normal euclidean dist formula
#because of third dimension i need dist
#used tutorial https://yordi.me/advent-of-code-2025-day-8/ for help

from math import dist

def merge_circuits(all_circuits, box_a_id, box_b_id):
    circuit_for_a = None
    circuit_for_b = None

    # find which circuit contains box a and b
    for circuit in all_circuits:
        if box_a_id in circuit:
            circuit_for_a = circuit
        if box_b_id in circuit:
            circuit_for_b = circuit

    #if they are in different circuits  merge them together
    if circuit_for_a is not circuit_for_b:
        circuit_for_a.update(circuit_for_b)
        all_circuits.remove(circuit_for_b)

numbers_array=[] #contains the parsed inputs
distances=[] #contains the calculated distances
with open("inputs","r") as f:
    for line in f:
        parts = line.strip().split(",")

        x = (int)(parts[0])
        y = (int)(parts[1])
        z = (int)(parts[2])
        numbers_array.append((x,y,z))

    #calculate all distances
    for i in range(len(numbers_array)):
        for j in range(i+1,len(numbers_array)):
            #p1 and 2 are the id of boxes
            p1,p2 = numbers_array[i],numbers_array[j]
            d = dist(p1,p2)
            distances.append(((i,j),d))
    #sort from shortest distance to longest
    distances.sort(key=lambda x: x[1])

    # create a starting set for every individual junction box
    circuits = [{i} for i in range(len(numbers_array))]

    # connect the 1000 closest pairs
    for i in range(1000):
        ((p1,p2),_) = distances[i]
        merge_circuits(circuits, p1, p2)

#take sizes of circuits
#sort biggest to smallest
#multiply top 3
sizes=[len(c) for c in circuits]
sizes.sort(reverse=True)
answer=sizes[0]*sizes[1]*sizes[2]

print(answer)




