import itertools

class moon:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.xVelocity = 0
        self.yVelocity = 0
        self.zVelocity = 0
    
    def energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.xVelocity) + abs(self.yVelocity) + abs(self.zVelocity))
    
    def __str__(self):
        return f"x:{self.x} y:{self.y} z:{self.z} xVel:{self.xVelocity} yVel:{self.yVelocity} zVel:{self.zVelocity}"
    
    def __repr__(self):
        return self.__str__()
    
    def point(self):
        return f"{self.x}, {self.y}, {self.z}"


if __name__ == "__main__":
    data = None
    with open("input.txt", 'r') as f:
        data = f.read().split('\n')
    
    moons = []

    # data = ['-1,0,2','2,-10,-7','4,-8,8', '3,5,-1']

    for newMoon in data:
        newMoon = newMoon.split(',')
        moons.append(moon(int(newMoon[0]), int(newMoon[1]), int(newMoon[2])))

    for step in range(1000):
        stepResult = ""
        print(f"step {step + 1}")
        pairs = itertools.combinations(range(len(moons)), 2)
        for pair in pairs:
            moon1 = pair[0]
            moon2 = pair[1]
            if moons[moon1].x < moons[moon2].x:
                moons[moon1].xVelocity += 1
                moons[moon2].xVelocity -= 1
            elif moons[moon1].x > moons[moon2].x:
                moons[moon1].xVelocity -= 1
                moons[moon2].xVelocity += 1
            
            if moons[moon1].y < moons[moon2].y:
                moons[moon1].yVelocity += 1
                moons[moon2].yVelocity -= 1
            elif moons[moon1].y > moons[moon2].y:
                moons[moon1].yVelocity -= 1
                moons[moon2].yVelocity += 1
            
            if moons[moon1].z < moons[moon2].z:
                moons[moon1].zVelocity += 1
                moons[moon2].zVelocity -= 1
            elif moons[moon1].z > moons[moon2].z:
                moons[moon1].zVelocity -= 1
                moons[moon2].zVelocity += 1
                    
        for updateMoon in range(len(moons)):
            moons[updateMoon].x += moons[updateMoon].xVelocity
            moons[updateMoon].y += moons[updateMoon].yVelocity
            moons[updateMoon].z += moons[updateMoon].zVelocity
            stepResult += moons[updateMoon].point()
            stepResult += "\n"
        print(stepResult)
        
    
    total = 0
    for printMoon in moons:
        total += printMoon.energy()
    print(total)