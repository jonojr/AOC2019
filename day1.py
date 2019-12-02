total = 0
with open("day1.txt", 'r') as f:
        lines = f.readlines()

        for line in lines:
            nextvaL = (int(line) // 3) - 2
            total += nextvaL

print(total)