def pathLength(obj, orbits):
    if orbits[obj][0] != None:
        return 1 + pathLength(orbits[obj][0], orbits)
    else:
        return 0

if __name__ == "__main__":
    with open("input.txt", 'r') as f:
        orbits = {}

        data = [x.split(')') for x in f.read().split('\n')][:-1]
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

        # print(orbits)
        total = 0
        for key in orbits.keys():
            total += pathLength(key, orbits)
    
        print(f"Total direct and indirect orbits: {total}")
