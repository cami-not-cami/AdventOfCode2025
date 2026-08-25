import itertools

light_diagramm = []
button_wiring = []
joltage = []


with open("inputs", "r") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        diagram_part, rest = line.split("]", 1)
        diagram = diagram_part.replace("[", "").strip()

        wiring_part, joltage_part = rest.split("{", 1)

        # parse numbers, clear } and split on commas
        j_nums = [
            int(x)
            for x in joltage_part.replace("}", "").split(",")
            if x.strip()
        ]

        #split on ( to isolate each buttons
        buttons = []
        for group in wiring_part.split("("):
            cleaned = group.replace(")", "").strip()
            if cleaned:
                buttons.append([int(x) for x in cleaned.split(",") if x.strip()])

        light_diagramm.append(diagram)
        button_wiring.append(buttons)
        joltage.append(j_nums)

#solves one row aka one machine
def solve_one(diagram, buttons_list):
    #this is the light diagram from the inputs
    target = list(diagram)
    #number of btn presses
    for number_press in range(len(buttons_list) + 1):
        #generates every unique combination of btns for the current number of presses
        for combination in itertools.combinations(range(len(buttons_list)), number_press):
            #resets all lights to off
            lights = ["."] * len(diagram)
            for btn_id in combination:
                #change the state of lights
                for light_id in buttons_list[btn_id]:
                    #flipping . becomes #
                    lights[light_id] = "#" if lights[light_id] == "." else "."
            #check if it matches the target
            if lights == target:
                #return nr of presses used
                return len(combination)
    return 0

total=0
for i in range(len(light_diagramm)):
    res = solve_one(light_diagramm[i],button_wiring[i])
    total += res

print(total)