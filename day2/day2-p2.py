class Main:
    def __init__(self):
        total = 0
        with open("inputs") as f:
            numberList = f.readlines()

            for l in numberList:
                idList = l.split(",")
                for id in idList:

                    individ = id.split("-")
                    num1 = int(individ[0])
                    num2 = int(individ[1])
                    for i in range(num1, num2 + 1):
                        #still comparing the strings to see if they are doubled
                        #if yes its a pattern so i add to total
                        text = str(i)
                        doubled = text + text
                        middle = doubled[1:-1]

                        if text in middle:
                            total += i

        print("Total of stuff:", total)


Main()