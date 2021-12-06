# Day 6, AOC 2021
import sys
inputfile = open(sys.argv[1], 'r')

init_fish = map(int,inputfile.read().strip().split(","))
# print(init_fish)

# Part 1

class School :

    SPAWN_AGE = 8
    RESET_AGE = 6

    def __init__(self, starting_fish) :
        self.fish_dict = [0]*(self.SPAWN_AGE+1)
        # for i in range(self.SPAWN_AGE+1) :
        #     self.fish_dict[i] = 0

        for fish in starting_fish :
            self.fish_dict[fish] += 1

        # print(self.fish_dict[0])

    def display_school(self) :
        print("Displaying school...")
        for i in range(self.SPAWN_AGE+1) :
            print("Fish at age %d: %d" %(i, self.fish_dict[i]))
        print("Total fish: %d" % self.count_fish())

    def count_fish(self) :
        count = 0
        # for key in self.fish_dict :
        #     count += self.fish_dict[key]
        for indiv_count in self.fish_dict :
            count += indiv_count
        return count

    def update_school(self) :

        # how many fish have reproduced?
        # count them, and then remove them from consideration. we'll handle those in the next block.
        repro_fish_count = self.fish_dict[0]
        # print("Num of new fish: %d" % repro_fish_count)
        self.fish_dict[0] = 0

        # NOW, go through remaining fish and decrement
        for i in range(1,self.SPAWN_AGE+1) :
            self.fish_dict[i-1] = self.fish_dict[i]

        self.fish_dict[self.SPAWN_AGE] = 0 # need to reset the eldest fish - that gets accounted for by the previous loop otherwise

        # for all of those fish, create the appropriate number of fish with the relevant age
        # and reset them to the reset age
        for i in range(repro_fish_count) :
            self.fish_dict[self.SPAWN_AGE] += 1
            self.fish_dict[self.RESET_AGE] += 1

print("Part 1\n")
part1_school = School(init_fish)
for i in range(80):
    part1_school.update_school()

part1_school.display_school()

print("Part 2\n")
part2_school = School(init_fish)
for i in range(256):
    if (i % 10 == 9) :
        print("Calculating day %d..." % (i+1))
    part2_school.update_school()

part2_school.display_school()
