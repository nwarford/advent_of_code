with open("input", "r") as file:
    # read file line by line
    content = file.readlines()

# Part 1
calibrationVals = []
for line in content :
    firstInt = str()
    lastInt = str()
    # print(line)
    # Get the first integer
    for i in line :
        if i.isdigit() :
            firstInt = i
            break
    
    # Get the last integer
    for i in reversed(line) :
        # print(i, end="")
        if i.isdigit() :
            # print("DIGIT")
            lastInt = i
            break
            # print(lastInt)
    print(firstInt, lastInt)

    calibrationVals.append(int(firstInt + lastInt))

# add up calibrationVals
print(sum(calibrationVals))