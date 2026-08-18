import csv
from operator import index

class Main:
    def __init__(self):
        total = 0
        with open("inputs") as f:
            numberList = f.readlines()

            #iterate each row
            for l in numberList:
                clean_list = l.strip()
                # Reset highest for each new row
                highest = 0

                #this is kind of like a bubble sort but instead of swapping elements i compare all possible pairs and take only the highest

                # iterate each tens digit so 81 -> 8
                for i in range(len(clean_list) - 1):
                    # next digit -> 1
                    for j in range(i + 1, len(clean_list)):
                        # create the combined nr so 81
                        combined_num = int(clean_list[i] + clean_list[j])

                        # if it is higher than the currently saved highest one
                        # overwrite it with the new highest
                        if combined_num > highest:
                            highest = combined_num

                # add highest from each row
                total += highest

            print(total)


Main()