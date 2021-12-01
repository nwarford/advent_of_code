# Day 1, AOC 2021

inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

firstLine = True
prevLine = 0
count = 0
for line in lines :
    if firstLine :
        prevLine = int(line)
        firstLine = False
    else :
        currLine = int(line)
        if currLine > prevLine :
            count += 1
        prevLine = currLine

print("count for part 1: %d" % count)

# part 2

def get_window(index) :
    try :
        A = int(lines[index])
        B = int(lines[index + 1])
        C = int(lines[index + 2])
        return A + B + C
    except Exception as ex :
        print("Exception " + ex + " has occurred.")

firstWindow = True
prevWindow = -1
count = 0
for i in range(len(lines)-2) :
    if firstWindow :
        prevWindow = get_window(i)
        firstWindow = False
    else :
        currWindow = get_window(i)
        if currWindow > prevWindow :
            count += 1
        prevWindow = currWindow

print("count for part 2: %d" % count)
