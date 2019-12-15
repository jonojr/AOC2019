import math
import collections

def findRequirements(lookupRecepies, material, quantity, leftovers):
    createQuantity = lookupRecepies[material][0]

    # print(material, lookupRecepies[material])
    
    # Check if there is any leftovers we can use
    if leftovers[material] != 0:
        if leftovers[material] < createQuantity:
            quantity -= leftovers[material]
            leftovers[material] = 0
        else:
            leftovers[material] -= createQuantity
            return 0

    reqQuantityMultiplier = math.ceil(quantity / createQuantity)

    leftovers[material] += (reqQuantityMultiplier * createQuantity) - quantity

    if lookupRecepies[material][1][0] == "ORE":
        return reqQuantityMultiplier * lookupRecepies[material][2][0]
    else:
        oreCount = 0
        for materialID in range(len(lookupRecepies[material][1])):
            oreCount += (findRequirements(lookupRecepies, lookupRecepies[material][1][materialID], reqQuantityMultiplier * lookupRecepies[material][2][materialID], leftovers))
        return oreCount


if __name__ == "__main__":
    recepies = None
    with open('Z:\\2019\\AOC2019\\Day 14\\input.txt', 'r') as f:
        recepies = f.read().split('\n')
        recepies = [x.split(' => ') for x in recepies]

    leftovers = collections.defaultdict(int)
    lookupRecepies = {}

    for recepie in recepies:
        creates = recepie[1].split(' ')[1]
        createCount = recepie[1].split(' ')[0]

        requires = recepie[0].split(', ')

        inputs = []
        inputCounts = []

        for requirements in requires:
            inputCounts.append(int(requirements.split(' ')[0]))
            inputs.append(requirements.split(' ')[1])

        lookupRecepies[creates] = (int(createCount), inputs, inputCounts)

    ORE_REQ = findRequirements(lookupRecepies, 'FUEL', 1, leftovers)
    FUEL_COUNT = 337075
    while ORE_REQ < 1000000000000:
        leftovers = collections.defaultdict(int)
        FUEL_COUNT += 1000
        print(FUEL_COUNT)
        ORE_REQ = findRequirements(lookupRecepies, 'FUEL', FUEL_COUNT, leftovers)
    
    while ORE_REQ > 1000000000000:
        leftovers = collections.defaultdict(int)
        FUEL_COUNT -= 1
        print(FUEL_COUNT)
        ORE_REQ = findRequirements(lookupRecepies, 'FUEL', FUEL_COUNT, leftovers)

    print(FUEL_COUNT, ORE_REQ)
