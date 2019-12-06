def pathSet(obj, orbits):
    if orbits[obj][0] != None:
        return set([obj]).union(pathSet(orbits[obj][0], orbits))
    else:
        return set([])

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        orbits = {}

        data = [x.split(')') for x in f.read().split('\n')]
        # print(data)

        for orbit in data:
            base = orbit[0]
            orbiter = orbit[1]
            # print(base, orbiter)

            if base in orbits.keys():
                orbits[base][1] += 1
            else:
                # print('Adding base to orbits')
                orbits[base] = [None, 1]

            if orbiter in orbits.keys():
                orbits[orbiter][0] = base
            else:
                orbits[orbiter] = [base, 0]

        transfers = 0

        you = 'YOU'
        santa = 'SAN'

        youToRoot = pathSet(you, orbits)
        santaToRoot = pathSet(santa, orbits)

        difference = youToRoot.symmetric_difference(santaToRoot)
        
        print(len(difference) - 2)
