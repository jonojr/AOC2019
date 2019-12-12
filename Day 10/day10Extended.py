import math

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

        Unless b==0, the result will have the same sign as b (so that when
        b is divided by it, the result comes out positive).
        """
    while b:
        a, b = b, a % b
    return a

def distance(aX, aY, bX, bY):
    return abs(aX - bX) + abs(aY - bY)

def axisDist(aX, bX):
    return abs(aX - bX)

def simplify_fraction(numer, denom):

    if denom == 0:
        return 1, 0

    # Remove greatest common divisor:
    common_divisor = gcd(numer, denom)
    (reduced_num, reduced_den) = (numer / common_divisor, denom / common_divisor)
    # Note that reduced_den > 0 as documented in the gcd function.

    return int(reduced_num), int(reduced_den)

def xyRatio(aX, aY, bX, bY):
    xDist = axisDist(aX, bX)
    yDist = axisDist(aY, bY)

    xRatio = simplify_fraction(xDist, yDist)[0]
    yRatio = simplify_fraction(xDist, yDist)[1]

    return xRatio, yRatio

def createSets(asteroidField):
    asteroids = set([])
    freeSpace = set([])

    for i in range(width):
        for j in range(height):
            if asteroidField[j][i] == '#':
                asteroids.add((i, j))
            else:
                freeSpace.add((i, j))
    return asteroids, freeSpace

def createOrdering(width, height):
    solution = [[0 for i in range(width)] for j in range(height)]

    for i in range(width):
        for j in range(height):
            theta =  (0.5*math.pi) -  math.atan2(-1 * (j - 28), i - 22)
            if theta < 0:
                theta = abs(theta) + (math.pi)
            theta = theta % (2  *math.pi)
            solution[i][j] = theta
    solution[22][28] = float("inf")
    return solution

def canSee(asteroid, asteroid2, asteroids):
    xRatio, yRatio = xyRatio(asteroid[0], asteroid[1], asteroid2[0], asteroid2[1])

    if asteroid[0] > asteroid2[0]:
        xDirectionMultiplyer = -1
    else:
        xDirectionMultiplyer = 1
    
    if asteroid[1] > asteroid2[1]:
        yDirectionMultiplyer = -1
    else:
        yDirectionMultiplyer = 1

    currentLocation = asteroid

    while currentLocation != asteroid2:
        currentLocation = (currentLocation[0] + (xDirectionMultiplyer * xRatio), currentLocation[1] + (yDirectionMultiplyer * yRatio))
        if currentLocation in asteroids and currentLocation != asteroid2:
            return False
    
    return True

def findSmallestCanSee(ordering, asteroids, minAngle):
    smallestAngle = float("inf")
    smallest = None
    for asteroid in asteroids:
        if canSee((22, 28), asteroid, asteroids):
            angle = ordering[asteroid[0]][asteroid[1]]
            if  angle < smallestAngle and angle > minAngle:
                smallestAngle = angle
                smallest = asteroid
    return smallest, smallestAngle

def toRelativeCord(asteroid):
    return (asteroid[1] - 28, asteroid[0] - 22)



if __name__ == "__main__":
    # asteroidField = []
    # with open("input.txt", 'r') as f:
    #     asteroidField = f.read().split('\n')
    
    asteroidField = ['#.#.##..#.###...##.#....##....###', '...#..#.#.##.....#..##.#...###..#', '####...#..#.##...#.##..####..#.#.', '..#.#..#...#..####.##....#..####.', '....##...#.##...#.#.#...#.#..##..', '.#....#.##.#.##......#..#..#..#..', '.#.......#.....#.....#...###.....', '#.#.#.##..#.#...###.#.###....#..#', '#.#..........##..###.......#...##', '#.#.........##...##.#.##..####..#', '###.#..#####...#..#.#...#..#.#...', '.##.#.##.........####.#.#...##...', '..##...#..###.....#.#...#.#..#.##', '.#...#.....#....##...##...###...#', '###...#..#....#............#.....', '.#####.#......#.......#.#.##..#.#', '#.#......#.#.#.#.......##..##..##', '.#.##...##..#..##...##...##.....#', '#.#...#.#.#.#.#..#...#...##...#.#', '##.#..#....#..##.#.#....#.##...##', '...###.#.#.......#.#..#..#...#.##', '.....##......#.....#..###.....##.', '........##..#.#........##.......#', '#.##.##...##..###.#....#....###.#', '..##.##....##.#..#.##..#.....#...', '.#.#....##..###.#...##.#.#.#..#..', '..#..##.##.#.##....#...#.........', '#...#.#.#....#.......#.#...#..#.#', '...###.##.#...#..#...##...##....#', '...#..#.#.#..#####...#.#...####.#', '##.#...#..##..#..###.#..........#', '..........#..##..#..###...#..#...', '.#.##...#....##.....#.#...##...##']
    width = len(asteroidField[0])
    height = len(asteroidField)
    # print(asteroidField)
    

    asteroids, freeSpace = createSets(asteroidField)


    asteroid = (22, 28)
    visibleAsteroids = set()
    for asteroid2 in asteroids:
        if asteroid != asteroid2:
            xRatio, yRatio = xyRatio(asteroid[0], asteroid[1], asteroid2[0], asteroid2[1])

            if asteroid[0] > asteroid2[0]:
                xDirectionMultiplyer = -1
            else:
                xDirectionMultiplyer = 1
            
            if asteroid[1] > asteroid2[1]:
                yDirectionMultiplyer = -1
            else:
                yDirectionMultiplyer = 1

            currentLocation = asteroid
            pathfree = True
            while currentLocation != asteroid2:
                currentLocation = (currentLocation[0] + (xDirectionMultiplyer * xRatio), currentLocation[1] + (yDirectionMultiplyer * yRatio))
                if currentLocation in asteroids and currentLocation != asteroid2:
                    pathfree = False
            
            if pathfree is True:
                visibleAsteroids.add(asteroid2)
    
    # print(visibleAsteroids)
    # print(len(visibleAsteroids))

    listVisibleAsteroids = list(visibleAsteroids)

    listVisibleAsteroids.sort()
    # print(listVisibleAsteroids)

    toExplode = [(-math.atan2(x[0] - 22, x[1] - 28), x) for x in listVisibleAsteroids]
    toExplode.sort()
    print(toExplode[199][1][0], toExplode[199][1][1])
   