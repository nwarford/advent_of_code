# Day 4, AOC 2021
import sys
inputfile = open(sys.argv[1], 'r')
lines = inputfile.read().splitlines()

draw_order = map(int,lines[0].split(","))
bingo_card_list = []

def parse_bingo_card(lines_index_start) :
    bingo_card = []
    for i in range(lines_index_start, lines_index_start + 5) :
        num_line = lines[i].split()
        for k in range(len(num_line)) :
            num_line[k] = int(num_line[k])
        bingo_card.append(num_line)

    for j in range(5) :
        # use this to record numbers that have been marked on this card
        bingo_card.append([0]*5)

    return bingo_card

def update_bingo_card(number, card) :
    for i in range(5) :
        try :
            number_index = card[i].index(number)
            # print("Found at %d" % number_index)
            card[i+5][number_index] = 1
        except ValueError :
            # print("Not found")
            continue

def check_victory(card) :
    for i in range(5) :
        winning_row = check_victory_row(card[i+5],card)
        if winning_row == True :
            return True
    for i in range(5) :
        winning_col = check_victory_col(i,card)
        if winning_col == True :
            return True

    return False

def check_victory_row(row,card) :
    for entry in row :
        if entry == 0 :
            return False
    # print("Winning row found")
    return True

def check_victory_col(col,card) :
    for i in range(5) :
        if card[i+5][col] == 0 :
            return False
    # print("Winning column found at column %d" % i)
    return True

def get_unmarked_sum(card) :
    sum = 0
    for i in range(5) :
        for j in range(5) :
            if card[i+5][j] == 0 :
                sum = sum + card[i][j]
    return sum

def part_1_winner() :
    for draw in draw_order :

        for card in bingo_card_list :
            update_bingo_card(draw,card)

        for card in bingo_card_list :
            if check_victory(card) == True :
                # print(card)
                # print(get_unmarked_sum(card))
                return get_unmarked_sum(card) * draw

for i in range(2,len(lines),6) :
    bingo_card_list.append(parse_bingo_card(i))

print("Final score for part 1: %d" % part_1_winner())

# Part 2

# Reparse bingo cards rather than try to reset

def part_2_winner() :
    for draw in draw_order :
        for card in bingo_card_list_2 :
            update_bingo_card(draw,card)

        for i in range(len(bingo_card_list_2)) :
            if check_victory(bingo_card_list_2[i]) == True :
                winners[i] = 1
                try :
                    nonwin_index = winners.index(0)
                except ValueError :
                    print(card)
                    print(draw)
                    return   get_unmarked_sum(card) * draw

bingo_card_list_2 = []
for i in range(2,len(lines),6) :
    bingo_card_list_2.append(parse_bingo_card(i))
winners = [0] * len(bingo_card_list_2)

print("Final score for part 2: %d" % part_2_winner())
