# day 2, 2020

inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

# part 1

def parse_password_count(text_line) :
    space_split = text_line.split(" ")
    # print(space_split)
    range_split = space_split[0].split("-")
    # print(range_split)
    min_count = int(range_split[0])
    max_count = int(range_split[1])
    character = space_split[1][0]
    num_occurrence = space_split[2].count(character)
    # print(character)
    # print("min count: %d\nmax count = %d\noccurrences = %d" % (min_count, max_count, num_occurrence))
    if ((num_occurrence >= min_count) and (num_occurrence <= max_count)):
        return 1
    else:
        return 0

count = 0
for line in lines:
    count += parse_password_count(line)

print("final count for part 1: %d" % count)

# part 2

def parse_password_pos(text_line) :
    space_split = text_line.split(" ")
    # print(space_split)
    range_split = space_split[0].split("-")
    # print(range_split)

    pos_1 = int(range_split[0]) - 1
    pos_2 = int(range_split[1]) - 1
    character = space_split[1][0]
    password_string = space_split[2]
    # print(character)
    # print("pos 1: %d\npos 2 = %d\n" % (pos_1, pos_2))

    num_correct = 0
    if password_string[pos_1] == character :
        num_correct += 1
    if password_string[pos_2] == character :
        num_correct += 1

    if num_correct == 1 :
        return 1
    else :
        return 0

count = 0
for line in lines:
    count += parse_password_pos(line)

print("final count for part 2: %d" % count)
