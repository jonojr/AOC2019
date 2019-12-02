def calculateFuel(mass):
    fuelMass = (mass // 3) - 2
    if (fuelMass <= 0):
        return 0
    else:
        # print(fuelMass)
        return fuelMass + calculateFuel(fuelMass)


total = 0
with open("day1.txt", 'r') as f:
        lines = f.readlines()

        for line in lines:
            nextvaL = calculateFuel(int(line))
            total += nextvaL

print(total)