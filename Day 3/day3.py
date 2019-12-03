def mapPath(path):
    position = [0,0]
    positions = set([])

    for direction in path:
        if direction[0] == 'R':
            for _ in range(int(direction[1:])):
                position[0] += 1
                positions.add((position[0], position[1]))

        elif  direction[0] == 'L':
            for _ in range(int(direction[1:])):
                position[0] -= 1
                positions.add((position[0], position[1]))

        elif  direction[0] == 'U':
            for _ in range(int(direction[1:])):
                position[1] += 1
                positions.add((position[0], position[1]))
        
        elif  direction[0] == 'D':
            for _ in range(int(direction[1:])):
                position[1] -= 1
                positions.add((position[0], position[1]))
    
    return positions

def manhattan(pos):
    return abs(pos[0]) + abs(pos[1])

if __name__ == "__main__":
    
    with open("input.txt", 'r') as f:
        bestDist = 1000000000

        data = f.read()
        data = data.split()

        first = data[0]
        second = data[1]

        first = first.split(',')
        second = second.split(',')

        firstpath = mapPath(first)
        secondpath = mapPath(second)

        overlaps = firstpath.intersection(secondpath)
        print(overlaps)

        for position in overlaps:
            distance = manhattan(position)
            if distance < bestDist:
                bestDist = distance
        
        print(bestDist)


