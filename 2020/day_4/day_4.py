# day 4, 2020
import re
inputfile = open('input.txt', 'r')

# Part 1

def sep_passports() :
    # separates the input file into lists of strings that make up a given passport
    all_passports = []
    passport = []
    for line in inputfile :
        # print(line)
        if line != "\n" :
            line = line.rstrip()
            passport.append(line)
        else :
            all_passports.append(passport)
            passport = []

    if passport != [] :
        # need to catch the last passport - it doesn't trigger if there's no new line
        all_passports.append(passport)

    return all_passports

def parse_passport(passport_list) :
    # input: list of lines that make out a passport
    # output: dictionary of appropriate values
    discrete_list = []
    passport_dict = {
        "byr" : "",
        "iyr" : "",
        "eyr" : "",
        "hgt" : "",
        "hcl" : "",
        "ecl" : "",
        "pid" : "",
        "cid" : ""
        }
    for string in passport_list :
        split_string = string.split(" ")
        for item in split_string :
            discrete_list.append(item)

    for item in discrete_list :
        sep_value = item.split(":")
        attr = sep_value[0]
        val = sep_value[1]
        passport_dict[attr] = val

    return passport_dict

def eval_passport(passport_dict) :
    # checks if a dictionary passport is valid
    for key in passport_dict :
        if passport_dict[key] == "" and key != 'cid' :
            # print("missing key: " + key)
            # print passport_dict
            return 0

    return 1

all_passports_unparsed = sep_passports()
# print("length of unparsed: %d" % len(all_passports_unparsed))
all_passports_parsed = []
for unparsed in all_passports_unparsed :
    all_passports_parsed.append(parse_passport(unparsed))

count = 0
for passport in all_passports_parsed :
    count = count + eval_passport(passport)

print("count for part 1: %d" % count)

# part 2
def eval_passport_key(passport_dict) :
    # checks if a dictionary passport is valid based on key criteria
    for key in passport_dict :
        if eval_key(key, passport_dict[key]) == False :
            return 0

    return 1

ecl_list = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]

def eval_key(key, value) :
    if value == '' and key != "cid" :
        return False

    if key == 'byr' :
        # try :
        year = int(value)
        if year >= 1920 and year <= 2002 :
            return True
        else :
            return False
        # except ValueError :
        #     return False

    elif key == 'iyr' :
        year = int(value)
        if year >= 2010 and year <= 2020 :
            return True
        else :
            return False

    elif key == 'eyr' :
        year = int(value)
        if year >= 2020 and year <= 2030 :
            return True
        else :
            return False

    elif key == 'hgt' :
        unit_index = len(value) - 2
        unit = value[unit_index:]
        try :
            number = int(value[:unit_index])
            if unit == "cm" :
                if number >= 150 and number <= 193 :
                    return True
                else :
                    return False
            else :
                if number >= 59 and number <= 76 :
                    return True
                else :
                    return False
        except ValueError :
            return False

    elif key == 'hcl' :
        if value[0] != "#" or len(value) != 7:
            return False
        else :
            if re.match('[0-9a-fA-F]', value[1:]) :
                return True
            else :
                return False

    elif key == 'ecl' :
        if value in ecl_list :
            return True
        else :
            return False
    elif key == 'pid' :
        if len(value) != 9 :
            return False
        else :
            try :
                pid_number = int(value)
                return True
            except ValueError :
                return False

count = 0
for passport in all_passports_parsed :
    count = count + eval_passport_key(passport)

print("count for part 2: %d" % count)
