inputfile = open('input.txt', 'r')

# Part 1

def sep_answers() :
    # separates the input file into lists of strings that make up a given answer
    all_answers = []
    answer = []
    for line in inputfile :
        # print(line)
        if line != "\n" :
            line = line.rstrip()
            answer.append(line)
        else :
            all_answers.append(answer)
            answer = []

    if answer != [] :
        # need to catch the last answer - it doesn't trigger if there's no new line
        all_answers.append(answer)

    return all_answers

def parse_answer_group(answer_group) :
    total_chars = []
    for answer in answer_group :
        for character in answer :
            if character not in total_chars :
                total_chars.append(character)

    return total_chars

all_answers = sep_answers()
count = 0
for answer_group in all_answers :
    total_chars = parse_answer_group(answer_group)
    count = count + len(total_chars)

print("sum for part 1: %d" % count)

# Part 2
def parse_answer_group_dict(answer_group) :
    char_dict = {}
    num_people = len(answer_group)
    # print("Number of people: %d" % num_people)
    for answer in answer_group :
        for character in answer :
            if character not in char_dict :
                char_dict[character] = 1
            else :
                char_dict[character] += 1

    sum = 0
    for key in char_dict :
        if char_dict[key] == num_people :
            sum += 1

    return sum

total_sum = 0
for answer_group in all_answers :
    total_sum = total_sum + parse_answer_group_dict(answer_group)

print("sum for part 2: %d" % total_sum)
