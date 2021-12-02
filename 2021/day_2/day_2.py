# Day 2, AOC 2021
import sys
inputfile = open(sys.argv[1], 'r')
lines = inputfile.read().splitlines()

# position[0] is horizontal, position[1] is depth
position = [0,0]

def update_position(split_instruction) :
    inst = split_instruction[0]
    num = split_instruction[1]
    if inst == "forward" :
        position[0] = position[0] + num
    elif inst == "down" :
        position[1] = position[1] + num
    elif inst == "up" :
        position[1] = position[1] - num

def parse_inst(inst_string) :
    split_string = inst_string.split(" ")
    split_string[1] = int(split_string[1])
    return split_string

for line in lines :
    update_position(parse_inst(line))

product = position[0] * position[1]
print("product for part 1: %d" % product)

# part 2

# position_aim[0] is horizontal, position_aim[1] is depth, position_aim[2] is aim
position_aim = [0,0,0]

def update_position_aim(split_instruction) :
    inst = split_instruction[0]
    num = split_instruction[1]
    if inst == "forward" :
        position_aim[0] = position_aim[0] + num
        depth_delta = num * position_aim[2]
        position_aim[1] = position_aim[1] + depth_delta
    elif inst == "down" :
        position_aim[2] = position_aim[2] + num
    elif inst == "up" :
        position_aim[2] = position_aim[2] - num

for line in lines :
    update_position_aim(parse_inst(line))

product = position_aim[0] * position_aim[1]
print("product for part 2: %d" % product)
