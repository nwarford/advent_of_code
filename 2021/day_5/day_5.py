# Day 5, AOC 2021
import sys
inputfile = open(sys.argv[1], 'r')
lines = inputfile.read().splitlines()

def parse_line(input_str) :
    # input: one line of the file
    # output: start and end coordinates in the form [x1,y1], [x2,y2]

    front,back = input_str.split(" -> ")

    start_coord = map(int,front.split(","))
    end_coord = map(int,back.split(","))
    return start_coord, end_coord

def get_max_coord(coord_list) :
    # input: a list of pairs of coordinates
    # output: the size x,y of our coordinate grid
    max_x = 0
    max_y = 0
    for entry in coord_list :
        for tuple in entry :
            if tuple[0] > max_x :
                max_x = tuple[0]
            if tuple[1] > max_y :
                max_y = tuple[1]

    # the coordinates are zero indexed, but i'm using these numbers for the absolute size of the array, so they need to be incremented.
    max_x += 1
    max_y += 1
    return max_x, max_y

def create_grid(x_size,y_size) :
    # input: size of grid in 2d
    # output: dict, indexed by tuples

    new_grid = { (i,j):0 for i in range(x_size) for j in range(y_size) }
    return new_grid

def update_line(coord, part1) :
    # input: the coordinates (we'll use the global grid here, since it should remain the same between calls), part1 is a boolean if we're working on part 1 so we can only do horiz/vert
    # no output, we'll edit grid directly

    start_x = coord[0][0]
    start_y = coord[0][1]
    end_x = coord[1][0]
    end_y = coord[1][1]

    if part1 :
        if not((start_x == end_x) or (start_y == end_y)) :
            return

    if start_x == end_x :
        y_range = get_range(start_y,end_y)
        for y in y_range :
            grid[(start_x,y)] += 1
    elif start_y == end_y :
        x_range = get_range(start_x,end_x)
        for x in x_range :
            grid[(x,start_y)] += 1
    else :
        # print("Diagonal alert! (%d, %d) -> (%d, %d)" % (start_x,start_y,end_x,end_y))
        # print(range(4,-1,-1))
        x_range = get_range(start_x,end_x)
        y_range = get_range(start_y,end_y)
        for i in range(len(x_range)) :
            x = x_range[i]
            y = y_range[i]
            # print("updating (%d, %d)" % (x,y))
            grid[(x,y)] +=1

def get_range(start,end) :
    # get the integers from start to end, regardless of which is greater *in correct order*
    if start < end :
        # if we're going (say) from 0 to 4, we want to return [0,1,2,3,4]. Range
        return(range(start,end+1))
    else :
        # if we're going 4 to 0, we need [4,3,2,1,0]
        return(range(start,end-1,-1))

def print_grid() :
    # since we're using a dict, some effort is required
    for i in range(max_coords[0]) :
        curr_row = []
        for j in range(max_coords[1]) :
            # I print these backwords because (x,y) makes logical sense but the as [row, col], but the examples in the prompt are printed opposite
            curr_row.append(grid[(j,i)])
        print(curr_row)

def eval_grid() :
    # thank goodness for list comprehension style syntax
    return sum(x > 1 for x in grid.values())

parsed_coord = []
for line in lines :
    parsed_coord.append(parse_line(line))

max_coords = get_max_coord(parsed_coord)
grid = create_grid(max_coords[0],max_coords[1])

for coord in parsed_coord :
    update_line(coord,True)

print("count for part 1: %d" % eval_grid())

# resetting for part 2 - clear removes all keys from the dict
grid.clear()
grid = create_grid(max_coords[0],max_coords[1])
for coord in parsed_coord :
    update_line(coord,False)

print("count for part 2: %d" % eval_grid())
