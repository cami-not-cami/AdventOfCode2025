additions = 0
multiplications = 0

with open("inputs") as f:
    lines = f.read().splitlines()

# pad lines so all columns align properly
max_len = max(len(line) for line in lines)
lines = [line.ljust(max_len) for line in lines]

number_rows = lines[:-1]
operator_row = lines[-1]

col = 0
while col < max_len:
    # skip spaces separating problems
    if all(lines[row][col] == " " for row in range(len(lines))):
        col += 1
        continue

    # grab column indices for current problem
    block_cols = []
    while col < max_len and not all(
        lines[row][col] == " " for row in range(len(lines))
    ):
        block_cols.append(col)
        col += 1

    # find operator at bottom of problem block
    op = None
    for c in block_cols:
        if operator_row[c] in ("+", "*"):
            op = operator_row[c]

    # read numbers vertically top to bottom
    nums = []
    for c in block_cols:
        digits = "".join(
            number_rows[r][c] for r in range(len(number_rows))
        ).strip()
        if digits:
            nums.append(int(digits))

    # calculate problem total
    if op == "+":
        additions += sum(nums)
    elif op == "*":
        result = 1
        for n in nums:
            result *= n
        multiplications += result

total = additions + multiplications

print(total)
