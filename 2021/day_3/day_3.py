# Day 3, AOC 2021
import sys, copy
inputfile = open(sys.argv[1], 'r')
lines = inputfile.read().splitlines()

# Part 1
str_len = len(lines[0])
max_val = (2 ** str_len) - 1

def max_at_index(index,list) :
    num_ones = 0
    num_zeros = 0

    for line in list :
        if line[index] == "0" :
            # print(line[index])
            num_zeros += 1
        else :
            num_ones += 1

    if num_ones >= num_zeros :
        return 1
    else :
        return 0

gamma_str = ""
for i in range(len(lines[0])) :
    gamma_str = gamma_str + str(max_at_index(i,lines))

gamma = int(gamma_str,2)
epsilon = max_val - gamma

print("gamma * epsilon for part 1: %d" % (gamma * epsilon))

# Part 2
def filter_list(list,char,index) :
    # Filters out elements of a list of strings where each string[index] == char
    new_list = []
    for string in list :
        if string[index] == char :
            new_list.append(string)

    return new_list

def get_part_2(diag) :
    input_str_length = len(lines[0])
    filtered_list = copy.deepcopy(lines)

    for i in range(input_str_length) :
        curr_max = max_at_index(i,filtered_list)
        if diag == "oxygen" :
            search_str = str(curr_max)
        elif diag == "co2" :
            if curr_max == 0 :
                search_str = "1"
            else :
                search_str = "0"

        filtered_list = filter_list(filtered_list, search_str, i)
        # print(filtered_list)
        if len(filtered_list) == 1 :
            return int(filtered_list[0],2)

oxygen = get_part_2("oxygen")
co2 = get_part_2("co2")

print("oxygen * co2 for part 2: %d" % (oxygen * co2))
