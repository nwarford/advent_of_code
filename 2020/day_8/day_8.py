from copy import deepcopy
inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

# Part 1
inst_array = []
for line in lines :
    # instruction, number, number of times run
    split_up = line.split(" ")
    split_up.append(0)
    split_up[1] = int(split_up[1])
    # print(split_up)
    inst_array.append(split_up)

def run_program(inst_array) :
    accumulator = 0
    index = 0
    while True :
        if index == len(inst_array) :
            return [accumulator, True]
        current_inst = inst_array[index]
        # print(current_inst)
        if current_inst[2] == 1 :
            current_inst[2] = 2
            # print(inst_array)
            return [accumulator, False]
        else :
            current_inst[2] = 1

        if current_inst[0] == 'acc' :
            accumulator = accumulator + current_inst[1]
            index += 1
            # print("acc, next index = " + str(index))
        elif current_inst[0] == 'nop' :
            index += 1
            # print("nop, next index = " + str(index))
        elif current_inst[0] == 'jmp' :
            index = index + current_inst[1]
            # print("jmp, next index = " + str(index))

inst_copy = deepcopy(inst_array)
[accumulator, terminate] = run_program(inst_copy)
for i in inst_array :
    i[2] = 0
print(inst_array)
print("accumulator for part 1: %d" % accumulator)

# Part 2
for index in range(len(inst_array)) :
    curr_inst = inst_array[index][0]
    for i in inst_array :
        i[2] = 0

    if curr_inst == 'acc' :
        continue
    elif curr_inst == 'jmp' :
        inst_array[index][0] = 'nop'
        # print("new inst: " + str(inst_array[index]))
        [accumulator, terminate] = run_program(inst_array)
        if terminate == True :
            print("accumulator for part 2: %d" % accumulator)
            break
        
        inst_array[index][0] = 'jmp'
    elif curr_inst == 'nop' :
        inst_array[index][0] = 'jmp'
        [accumulator, terminate] = run_program(inst_array)
        if terminate == True :
            print("accumulator for part 2: %d" % accumulator)
            break

        inst_array[index][0] = 'nop'

# print(inst_array)
