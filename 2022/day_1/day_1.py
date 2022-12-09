

# inputfile = open('test.txt', 'r')
inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

# takes input, divides elves into arrays of each elf's individual inventory
def createElves() :
    elflist = []
    currElf = []
    for line in lines:
        if line == "" :
            elflist.append(currElf)
            currElf = []
            next
        else :
            currElf.append(int(line))

    elflist.append(currElf)
    return elflist


elves = createElves()

# part 1
max = 0

for elf in elves :
    currSum = 0
    for inv in elf :
        currSum += inv

    if currSum > max :
        max = currSum

print("Maximum inventory: %d" % max)

top_max = 0
second_max = 0
third_max = 0

for elf in elves :
    currSum = 0
    for inv in elf :
        currSum += inv

    if currSum > third_max :
        if currSum > second_max :
            if currSum > top_max :
                third_max = second_max
                second_max = top_max
                top_max = currSum
            else :
                third_max = second_max
                second_max = currSum
        else :
            third_max = currSum

print("Top max: %d" % top_max)
print("Second max: %d" % second_max)
print("Third max: %d" % third_max)
print("Total: %d" % (top_max + second_max + third_max))