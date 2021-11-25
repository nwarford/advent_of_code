# day 3, 2020

inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

# part 1

def update_position(start_pos, length, horiz, vert) :
    start_x = start_pos[0]
    end_x = (start_x + horiz) % length

    start_y = start_pos[1]
    end_y = start_y + vert

    return([end_x, end_y])

def check_tree(x, y) :
    line = lines[y]
    if line[x] == "#" :
        return 1
    else :
        return 0

def eval_slope(right, down) :
    position = [0, 0]
    count = 0
    for i in range(0, len(lines), down) :
        new_position = update_position(position, len(lines[i]), right, down)
        new_x = new_position[0]
        new_y = new_position[1]
        if new_y >= len(lines) :
            break
        # print("new x: %d\nnew y: %d" % (new_x, new_y))
        count = count + check_tree(new_x, new_y)
        position = new_position

    return count

print("count part 1: %d" % eval_slope(3,1))

# part 2
slope_evaluations = [[1,1], [3,1], [5,1], [7,1],[1,2]]

product = 1
for pair in slope_evaluations :
    tree_count = eval_slope(pair[0],pair[1])
    product = product * tree_count

print("product part 2: %d" % product)
