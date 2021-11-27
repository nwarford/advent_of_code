inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

# Part 1
class BagRule :
    def __init__(self, input_string) :
        source_color_string = input_string.split(" contain ")
        # print(source_color_string)
        bags_index = source_color_string[0].index(" bag")
        # print(bags_index)
        trunc_source_color = source_color_string[0][:bags_index]
        self.source_color = trunc_source_color

        self.contain_dict = {}
        contain_rules_long = source_color_string[1].split(", ")
        # print(contain_rules_long)
        contain_rules_short = []
        for string in contain_rules_long :
            # print(string)
            bag_start = string.index(' bag')
            contain_rules_short.append(string[:bag_start])

        # print(contain_rules_short)
        for rule in contain_rules_short :
            try :
                first_space = rule.index(" ")
                number = int(rule[:first_space])
                # print(number)
                color_start = first_space + 1
                color = rule[color_start:]
                self.contain_dict[color] = number
            except ValueError :
                self.contain_dict = {}

    def __str__(self) :
        return 'bag color: ' + self.source_color + '; contains ' + str(self.contain_dict)

def find_container(source_bag, seek_color) :
    print("is it in " + source_bag.source_color + "?")
    if seek_color in source_bag.contain_dict :
        # print("yes, current count = " + str(count + 1))
        return 1
    elif source_bag.contain_dict == {} :
        # print("no, this is a leaf")
        return 0
    else :
        # print(source_bag.contain_dict)
        # print("no, but we can keep looking")
        tempsum = 0
        for key in source_bag.contain_dict :
            # print(key)
            tempsum = tempsum + find_container(bag_rule_dict[key],seek_color)
        if tempsum > 0 :
            return 1
        else :
            return 0


bag_rule_dict = {}
for line in lines :
    new_bag_rule = BagRule(line)
    bag_rule_dict[new_bag_rule.source_color] = new_bag_rule
    # bag_rule_list.append(sublist)

# print(bag_rule_dict)
count = 0
run_long = False
if run_long :
    for color in bag_rule_dict :
        if color != 'shiny gold' :
            # print("current color: " + color)
            count = count + find_container(bag_rule_dict[color], 'shiny gold')

# print(len(lines))
print('count for part 1: %d' % count)

# part 2
def count_bags(source_bag) :
    if source_bag.contain_dict == {} :
        # print(source_bag.source_color + " is empty")
        return 0
    else :
        sub_sum = 0
        current_bags = 0
        for key in source_bag.contain_dict :
            current_bags = current_bags + source_bag.contain_dict[key] + (count_bags(bag_rule_dict[key]) * source_bag.contain_dict[key])

        return sub_sum + current_bags

print(count_bags(bag_rule_dict['shiny gold']))
