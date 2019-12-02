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
    position = 0
    while memory[position] != 99:
        memory, position = process_code(memory, position)
    
    return memory[0]

position = 0
with open("day2.txt", 'r') as f:
    program = f.read()
    program = program.split(',')

    program = list(map(int, program))

    # init program to required values
    program[1] = 12
    program[2] = 2

    run(program)

print(f"Result: {program[0]}")