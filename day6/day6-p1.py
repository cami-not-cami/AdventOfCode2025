additions=0
multiplications=0
with open("inputs") as f:
    rows = [line.split() for line in f]

    for a, b, c,d, op in zip(*rows[:4], rows[4]):
            nums = map(int, (a, b, c,d))

            if op == "+":
                additions += sum(nums)
            elif op == "*":
                result = 1
                for n in nums:
                    result *= n
                multiplications += result

total = additions + multiplications

print( total  )