import copy
import itertools

class intcodePC:
    def __init__(self, program, inputs):
        self.program = copy.deepcopy(program)
        self.inputs = inputs
        self.outputs = []

        self.position = 0

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
            else:
                param1 = program[position + 1]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            else:
                param2 = program[position + 2]

            # print(f"Adding {param1} to {param2} equalling {param1 + param2} saving at {program[position + 3]}\tParameters: {program[position + 1]} {program[position + 2]} {program[position + 3]}\tParameter modes: {first_parameter_mode} {second_parameter_mode} {third_parameter_mode}")
            program[program[position + 3]] = param1 + param2

            position += 4   # increment the position

        elif (opcode == '02' or opcode == '2'):
            # Multiplication code
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            else:
                param1 = program[position + 1]
            
            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            else:
                param2 = program[position + 2]

            # print(f"Multiplying {param1} with {param2} equalling {param1 * param2} saving at {program[position + 3]}\tParameter modes: {first_parameter_mode} {second_parameter_mode} {third_parameter_mode}")
            program[program[position + 3]] = param1 * param2
            position += 4   # increment the position

        elif (opcode == '03' or opcode == '3'):
            # Input
            while not self.inputs:  # Wait for input
                pass

            if first_parameter_mode == 0:
                program[program[position + 1]] = self.inputs[0]
                # print(f"Input: 1\t{program[position + 1]}\tMode: 0")
            else:
                program[position + 1] = self.inputs[0]
                # print(f"Input: 1\t{program[position + 1]}\tMode: 1")
            position += 2   # increment the position
            self.inputs = self.inputs[1:]

        elif (opcode == '04' or opcode == '4'):
            # Output
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            else:
                param1 = program[position + 1]
            print(f"Output: {param1}\t{program[position + 1]}\tMode: {first_parameter_mode}")
            self.outputs.append(param1)
            position += 2   # increment the position
        
        elif (opcode == '05' or opcode == '5'):
            # Jump if True
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            else:
                param1 = program[position + 1]

            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            else:
                param2 = program[position + 2]
        
            if param1 != 0:
                position = param2
            else:
                position += 3   # increment the position

        elif (opcode == '06' or opcode == '6'):
            # Jump if False
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            else:
                param1 = program[position + 1]

            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            else:
                param2 = program[position + 2]
        
            if param1 == 0:
                position = param2
            else:
                position += 3   # increment the position

        elif (opcode == '07' or opcode == '7'):
            # Less than
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            else:
                param1 = program[position + 1]

            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            else:
                param2 = program[position + 2]
        
            if param1 < param2:
                program[program[position + 3]] = 1
            else:
                program[program[position + 3]] = 0
            position += 4   # increment the position

        elif (opcode == '08' or opcode == '8'):
            # Equal
            if first_parameter_mode == 0:
                param1 = program[program[position + 1]]
            else:
                param1 = program[position + 1]

            if second_parameter_mode == 0:
                param2 = program[program[position + 2]]
            else:
                param2 = program[position + 2]
        
            if param1 == param2:
                program[program[position + 3]] = 1
            else:
                program[program[position + 3]] = 0
            position += 4   # increment the position

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


def amp(program, phase):
    return intcodePC(program, [phase])

def ampChain(program, phases):
    A = amp(program, phases[0])
    B = amp(program, phases[1])
    C = amp(program, phases[2])
    D = amp(program, phases[3])
    E = amp(program, phases[4])
    amps = {'A': A, 'B': B, 'C': C, 'D': D, 'E': E}

    ampList = ['A', 'B', 'C', 'D', 'E']
    
    position = 0
    previous = 0

    while True:
        currentAmp = amps[ampList[position]]
        currentAmp.inputs.append(previous)
        result = currentAmp.getNextOutput()

        if result != None:
            previous = result
        else:
            if ampList[position] == 'E':
                print(ampList[position])
                return previous
        position += 1
        position %= len(ampList)

if __name__ == "__main__":

    # with open("input.txt", 'r') as f:
    #     incomingMemory = f.read()
    #     incomingMemory = incomingMemory.split(',')

    #     incomingMemory = list(map(int, incomingMemory))
        # program = copy.deepcopy(incomingMemory)

    incomingMemory = [3,8,1001,8,10,8,105,1,0,0,21,34,59,76,101,114,195,276,357,438,99999,3,9,1001,9,4,9,1002,9,4,9,4,9,99,3,9,102,4,9,9,101,2,9,9,102,4,9,9,1001,9,3,9,102,2,9,9,4,9,99,3,9,101,4,9,9,102,5,9,9,101,5,9,9,4,9,99,3,9,102,2,9,9,1001,9,4,9,102,4,9,9,1001,9,4,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,1002,9,3,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,2,9,4,9,3,9,102,2,9,9,4,9,99,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,1001,9,1,9,4,9,99,3,9,102,2,9,9,4,9,3,9,1001,9,1,9,4,9,3,9,1001,9,1,9,4,9,3,9,102,2,9,9,4,9,3,9,1001,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,101,2,9,9,4,9,3,9,102,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,99,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,2,9,9,4,9,3,9,101,1,9,9,4,9,3,9,1002,9,2,9,4,9,3,9,1002,9,2,9,4,9,3,9,1001,9,1,9,4,9,3,9,101,2,9,9,4,9,99]

    highest = 0
    for phase in list(itertools.permutations([5, 6, 7, 8, 9])):
        result = ampChain(incomingMemory, phase)
        if result > highest:
            highest = result
    print(highest)
