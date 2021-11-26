inputfile = open('input.txt', 'r')
lines = inputfile.read().splitlines()

#part 1
def find_seat(string) :
    # need to redefine these every time we call find_seat
    plane_row = range(128)
    plane_col = range(8)

    row_list = list(string[:7])
    col_list = list(string[7:])
    row_num = find_row(row_list, plane_row)
    col_num = find_col(col_list,plane_col)

    return [row_num, col_num]

def find_row(row_list, plane_row) :
    if len(plane_row) == 1 :
        return plane_row[0]
    else :
        halfway = len(plane_row) / 2
        instruction = row_list.pop(0)
        if instruction == "F" :
            return find_row(row_list,plane_row[:halfway])
        else :
            return find_row(row_list,plane_row[halfway:])

def find_col(col_list, plane_col) :
    if len(plane_col) == 1 :
        return plane_col[0]
    else :
        halfway = len(plane_col) / 2
        instruction = col_list.pop(0)
        if instruction == "L" :
            return find_col(col_list,plane_col[:halfway])
        else :
            return find_col(col_list,plane_col[halfway:])

max = 0
for line in lines :
    seat_nums = find_seat(line)
    seat_ID = seat_nums[0] * 8 + seat_nums[1]
    if seat_ID > max :
        max = seat_ID

print("max seat ID: %d" % max)

# part 2
occupied = [0] * (128 * 8)
for line in lines :
    seat_nums = find_seat(line)
    seat_ID = seat_nums[0] * 8 + seat_nums[1]
    occupied[seat_ID] = 1

print("my seat: %d" % occupied.index(0,48,916))
