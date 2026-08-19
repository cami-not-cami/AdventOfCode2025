class Main:
    def __init__(self):
        total=0
        with open("inputs") as f:
            numberList = f.readlines()

            for l in numberList:
                idList = l.split(",")
                for id in idList:

                    individ =id.split("-")
                    num1=int(individ[0])
                    num2=int(individ[1])
                    for i in range(num1,num2 +1):
                        string=str(i)
                        length = len(string)
                        if length % 2 == 0:
                            half_nr = length // 2
                            first = string[:half_nr]
                            second = string[half_nr:]
                            if(first == second):
                                total+=i

        print("Total of stuff:", total)




Main()