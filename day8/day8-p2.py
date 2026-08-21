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

    #if they are in different circuits  merge them together and remove it from the total
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

#loop through distances
for i in range(len(distances)):
    ((p1, p2), _) = distances[i]
    #merge them all again
    merge_circuits(circuits, p1, p2)
    #stop when we have one circuit instead of limiting to 1k
    if len(circuits) == 1:
        break
#p1 and p2 are now the final ids of the boxes
x_coord= numbers_array[p1][0]
y_coord= numbers_array[p2][0]

answer= x_coord * y_coord

print(answer)




