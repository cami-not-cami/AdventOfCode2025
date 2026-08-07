class Main:
    def __init__(self):
        self.currentIndex = 50
        self.passwordNr =0
        with open("inputs") as f:
            inputsList = f.read().splitlines()

            for right in inputsList:
                if 'R' in right:
                    self.isPlus = True
                    number = self.parseInput(right)
                else:
                    self.isPlus = False
                    number = self.parseInput(right)

                self.calculate(number, self.isPlus)
                print(f"Current Index: {self.currentIndex}, Password Nr: {self.passwordNr}")


    def parseInput(self, input):
        parsedDigits= "".join(c for c in input if c.isdigit())
        number = int(parsedDigits)
        return number


    def calculate(self, number, isPlus):
        #if self.currentIndex == 0 :
            #self.passwordNr += 1

        if isPlus:
            self.passwordNr += (self.currentIndex + number) //100
            self.currentIndex = (self.currentIndex + number) % 100
        else:

            if self.currentIndex > 0 and (self.currentIndex - number) <= 0:
                remainingSteps = number - self.currentIndex
                self.passwordNr += 1 + (remainingSteps // 100)

            elif self.currentIndex == 0:
                self.passwordNr += number // 100

            self.currentIndex = (self.currentIndex - number) % 100





Main()