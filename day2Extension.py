import copy

def process_code(program, position):
    # Process the opcode at this position

    if(program[position] == 1):
        # Addition code
        program[program[position + 3]] = program[program[position + 1]] + program[program[position + 2]]
        position += 4   # increment the position

    elif (program[position] == 2):
        # Multiplication code
        program[program[position + 3]] = program[program[position + 1]] * program[program[position + 2]]
        position += 4   # increment the position

    else:
        print("Invalid Opcode")
        # invalid Opcode
        pass
    return program, position

def run(memory):
    # Run the program given in memory
    position = 0
    while memory[position] != 99:
        memory, position = process_code(memory, position)
    
    return memory[0]


if __name__ == "__main__":
    noun = 0
    verb = 0

    with open("day2.txt", 'r') as f:
        incomingMemory = f.read()
        incomingMemory = incomingMemory.split(',')

        incomingMemory = list(map(int, incomingMemory))

        for i in range(99):
            for j in range(99):
                testMemory = copy.deepcopy(incomingMemory)
                testMemory[1] = i
                testMemory[2] = j

                if run(testMemory) == 19690720:
                    noun = i
                    verb = j

    print(f"Result: {100 * noun + verb}")