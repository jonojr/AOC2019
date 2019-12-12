from math import atan2, pi, gcd

grid = open('input.txt').read().strip().split('\n')
x, y = 22, 28

def count(l, k):
    a = y - k
    b = x - l
    if b == 0:
        a = a // abs(a)
    elif a == 0:
        b = b // abs(b)
    else:
        d = gcd(abs(a), abs(b))
        a = a // d
        b = b // d
    
    s = k + a
    t = l + b
    
    result = 0
    while s != y or t != x:
        if grid[s][t] == '#':
            result += 1
        s += a
        t += b
    return result

coordinates = [(j, i) for i in range(len(grid)) for j in range(len(grid[0])) if grid[i][j] == '#' and (i != y or j != x)]
coordinates.sort(key=lambda k: (count(*k), -atan2(k[0] - x, k[1] - y)))
print(coordinates)
print(coordinates[199][0] * 100 + coordinates[199][1])
