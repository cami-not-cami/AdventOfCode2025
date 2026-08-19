from operator import index

class Main:
    def __init__(self):
        total = 0
        with open("inputs") as f:
            numberList = f.readlines()

            for l in numberList:
                clean_list = l.strip()

                #12 digits is maximum
                remove = len(clean_list) - 12
                stack = []
                                #stack.append(1)  # Push
                                #stack[-1]  # Peek
                                #stack.pop()  # Pop

                for digit in clean_list:
                    # if the current digit is bigger than the last saved digit
                    # throw away the smaller digit if we still have removals left
                    while stack and remove > 0 and stack[-1] < digit:
                        stack.pop()
                        remove -= 1
                    stack.append(digit)

                # keep only the first 12 digits
                highest = int("".join(stack[:12]))
                total += highest

            print("Total for batteries:", total)


Main()