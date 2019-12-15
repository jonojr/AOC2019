import copy
import itertools

class intcodePC:
    def __init__(self, program, inputs):
        self.program = copy.deepcopy(program)
        self.inputs = inputs
        self.outputs = []

        self.position = 0
        self.relativeBase = 0

        self.halted = False

    def process_code(self, position):
        # Process the opcode at this position
        program = self.program

        strOperation = str(program[position])
        if(len(strOperation) > 1):
            opcode = strOperation[-2:]
            if(len(strOperation) > 2):
                first_parameter_mode = int(strOperation[-3])
            else:
                first_parameter_mode = 0
            
            if(len(strOperation) > 3):
                second_parameter_mode = int(strOperation[-4])
            else:
                second_parameter_mode = 0
            
            if(len(strOperation) > 4):
                third_parameter_mode = int(strOperation[-5])
            else:
                third_parameter_mode = 0
    
        else:
            opcode = strOperation
            first_parameter_mode = 0
            second_parameter_mode = 0
            third_parameter_mode = 0
            
        # print(f"{strOperation} opcode: {opcode}\tParameters: {program[position + 1]} {program[position + 2]} {program[position + 3]}\tParameter modes: {first_parameter_mode} {second_parameter_mode} {third_parameter_mode}")
        
        # print(opcode, str(program[position]))

        if(opcode == '01' or opcode == '1'):
            # Addition code
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            elif second_parameter_mode == 1:
                param2 = program[position + 2]
            elif second_parameter_mode == 2:
                param2 = program[self.relativeBase + program[position + 2]]

            # print(f"Adding {param1} to {param2} equalling {param1 + param2} saving at {program[position + 3]}\tParameters: {program[position + 1]} {program[position + 2]} {program[position + 3]}\tParameter modes: {first_parameter_mode} {second_parameter_mode} {third_parameter_mode}")
            result = param1 + param2

            if third_parameter_mode == 0:
                program[program[position + 3]] = result
            elif third_parameter_mode == 2:
                program[self.relativeBase + program[position + 3]] = result

            position += 4   # increment the position

        elif (opcode == '02' or opcode == '2'):
            # Multiplication code
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            elif second_parameter_mode == 1:
                param2 = program[position + 2]
            elif second_parameter_mode == 2:
                param2 = program[self.relativeBase + program[position + 2]]

            result = param1 * param2

            if third_parameter_mode == 0:
                program[program[position + 3]] = result
            elif third_parameter_mode == 2:
                program[self.relativeBase + program[position + 3]] = result
            # print(f"Multiplying {param1} with {param2} equalling {param1 * param2} saving at {program[position + 3]}\tParameter modes: {first_parameter_mode} {second_parameter_mode} {third_parameter_mode}")
            position += 4   # increment the position

        elif (opcode == '03' or opcode == '3'):
            # Input
            if not self.inputs:  # Wait for input
                print("Waiting for input")
                return program, position 

            if first_parameter_mode == 0:
                program[program[position + 1]] = self.inputs[0]
                # print(f"Input: 1\t{program[position + 1]}\tMode: 0")
            elif first_parameter_mode == 1:
                program[position + 1] = self.inputs[0]
            elif first_parameter_mode == 2:
                program[self.relativeBase + program[position + 1]] = self.inputs[0]
            
                # print(f"Input: 1\t{program[position + 1]}\tMode: 1")
            position += 2   # increment the position
            self.inputs = self.inputs[1:]

        elif (opcode == '04' or opcode == '4'):
            # Output
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]

            # print(f"Output: {param1}\tMode: {first_parameter_mode}")
            self.outputs.append(param1)
            position += 2   # increment the position
        
        elif (opcode == '05' or opcode == '5'):
            # Jump if True
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            elif second_parameter_mode == 1:
                param2 = program[position + 2]
            elif second_parameter_mode == 2:
                param2 = program[self.relativeBase + program[position + 2]]
        
            if param1 != 0:
                position = param2
            else:
                position += 3   # increment the position

        elif (opcode == '06' or opcode == '6'):
            # Jump if False
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            elif second_parameter_mode == 1:
                param2 = program[position + 2]
            elif second_parameter_mode == 2:
                param2 = program[self.relativeBase + program[position + 2]]
        
            if param1 == 0:
                position = param2
            else:
                position += 3   # increment the position

        elif (opcode == '07' or opcode == '7'):
            # Less than
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            elif second_parameter_mode == 1:
                param2 = program[position + 2]
            elif second_parameter_mode == 2:
                param2 = program[self.relativeBase + program[position + 2]]
        

            if param1 < param2:
                result = 1
            else:
                result = 0
            
            if third_parameter_mode == 0:
                program[program[position + 3]] = result
            elif third_parameter_mode == 2:
                program[self.relativeBase + program[position + 3]] = result
            
            position += 4   # increment the position

        elif (opcode == '08' or opcode == '8'):
            # Equal
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            elif second_parameter_mode == 1:
                param2 = program[position + 2]
            elif second_parameter_mode == 2:
                param2 = program[self.relativeBase + program[position + 2]]
        
            if param1 == param2:
                result = 1
            else:
                result = 0
            
            if third_parameter_mode == 0:
                program[program[position + 3]] = result
            elif third_parameter_mode == 2:
                program[self.relativeBase + program[position + 3]] = result

            position += 4   # increment the position

        elif (opcode == '09' or opcode == '9'):
            # Relative base offset
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            elif first_parameter_mode == 1:
                param1 = program[position + 1]
            elif first_parameter_mode == 2:
                param1 = program[self.relativeBase + program[position + 1]]

            self.relativeBase += param1
            position += 2   # increment the position

        else:
            print(f"Invalid Opcode {opcode}")
            # invalid Opcode
            pass
        return program, position

    def run(self):
        # Run the program given in memory
        while self.program[self.position] != 99:
            self.program, self.position= self.process_code(self.position)

        self.halted = True
        return self.outputs

    def getNextOutput(self):
        numExistingOutputs = len(self.outputs)
        while self.program[self.position] != 99 and len(self.outputs) == numExistingOutputs:
            self.program, self.position= self.process_code(self.position)

        if numExistingOutputs < len(self.outputs):
            return self.outputs[-1]
        
        if self.program[self.position] == 99:
            return None

        return self.outputs[-1]

class node:
    def __init__(this, pc, distance=0, previous=0):
        this.pc = pc
        this.distance = distance
        this.previous = previous

def inverseDirection(direction):
    if direction == 1:
        return 2
    if direction == 2:
        return 1
    if direction == 3:
        return 4
    if direction == 4:
        return 3
    else:
        print(f"UNKNOWN DIRECTION {direction}")
        return None

WALL = 0
EMPTY = 1
OXYGEN = 2

NORTH = (0, 1)
SOUTH = (0, -1)
EAST = (1, 0)
WEST = (-1, 0)

directions = set([1, 2, 3, 4])


def findOxySource(nodes):
    while nodes != []:
        droid = nodes[0]
        possibleDirections = directions - set([droid.previous])
        # print(possibleDirections)
        for direction in possibleDirections:
            newDroid = copy.deepcopy(droid)
            newDroid.pc.inputs.append(direction)

            result = newDroid.pc.getNextOutput()
            # print(direction, result)
            if result != WALL:
                newDroid.previous = inverseDirection(direction)
                newDroid.distance += 1
                nodes.append(newDroid)
            if result == OXYGEN:
                print(f"SOLUTION FOUND! {newDroid.distance}")
                return newDroid

        nodes = nodes[1:]
        # print(nodes[0].distance, len(nodes))


def floodFill(nodes):
    while nodes != []:
        droid = nodes[0]
        possibleDirections = directions - set([droid.previous])
        # print(possibleDirections)
        for direction in possibleDirections:
            newDroid = copy.deepcopy(droid)
            newDroid.pc.inputs.append(direction)

            result = newDroid.pc.getNextOutput()
            # print(direction, result)
            if result != WALL:
                newDroid.previous = inverseDirection(direction)
                newDroid.distance += 1
                nodes.append(newDroid)

        if nodes[1:] == []:
            return nodes[0]
        nodes = nodes[1:]
        print(nodes[0].distance, len(nodes))

if __name__ == "__main__":
    program = None
    with open("input.txt", 'r') as f:
        program = f.read().split(',')
        program = [int(x) for x in program]
    
    program.extend([0 for _ in range(10000)])

    droid = intcodePC(program, [])

    currentLocation = EMPTY

    nodes = [node(droid, 0)]

    print("Finding OXY")
    startNode = findOxySource(nodes)
    startNode.distance = 0
    startNode.previous = 0

    print("Flooding")
    print(floodFill([startNode]).distance)
    