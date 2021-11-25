# Day 1, AOC 2020

inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

# part 1
for i in range(len(lines)) :
    lines[i] = int(lines[i])

for i in range(len(lines)) :
    start_num = lines[i]

    for j in range(i+1,len(lines)) :
        if (lines[i] + lines[j] == 2020) :
            print(lines[i]*lines[j])

# part 2

for i in range(len(lines)) :
    start_num = lines[i]

    for j in range(i+1,len(lines)) :
        sum = lines[i] + lines[j]
        if (sum < 2020) :
            for k in range(j+1, len(lines)) :
                if (lines[k] + sum == 2020) :
                    print(lines[i]*lines[j]*lines[k])
