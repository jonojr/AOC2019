import copy

def process_code(program, position):
    # Process the opcode at this position

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
        # Only input is 1 for now
        if first_parameter_mode == 0:
            program[program[position + 1]] = 1
            # print(f"Input: 1\t{program[position + 1]}\tMode: 0")
        else:
            program[position + 1] = 1
            # print(f"Input: 1\t{program[position + 1]}\tMode: 1")
        position += 2   # increment the position

    elif (opcode == '04' or opcode == '4'):
        # Output
        if first_parameter_mode == 0:
            param1 = program[program[position + 1]]
        else:
            param1 = program[position + 1]
        print(f"Output: {param1}\t{program[position + 1]}\tMode: {first_parameter_mode}")
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

def run(memory):
    # Run the program given in memory
    position = 0
    while memory[position] != 99:
        memory, position = process_code(memory, position)
    
    return memory[0]


if __name__ == "__main__":

    with open("input.txt", 'r') as f:
        incomingMemory = f.read()
        incomingMemory = incomingMemory.split(',')

        incomingMemory = list(map(int, incomingMemory))

        run(incomingMemory)