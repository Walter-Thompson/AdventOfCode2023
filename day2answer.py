#Point to input data location
input_file = r"C:\Users\walte\Documents\GitHub\AdventOfCode2023\Inputs\day2.txt"

#Read input data file
with open(input_file) as file:
    data = [line.rstrip() for line in file]

#------------ PART 1 -----------#
maxima = {"red":12,"green":13,"blue":14}

valid_game_ids = []
#Each game we need to get the id (split left of colon)
for game in data:
    invalid_game = False
    game_id = game.split(":")[0].split()[1]
    game_results = game.split(": ")[1].split("; ")

    for set in game_results:
        single_choices = set.split(", ")
        for choice in single_choices:
            number = int(choice.split()[0])
            colour = choice.split()[1]
            if number > maxima[colour]:
                invalid_game = True
                
    if invalid_game == False:
        valid_game_ids.append(int(game_id))
   
valid_game_id_sum = sum(valid_game_ids)
print("Part 1 answer is:",valid_game_id_sum)

#------------ PART 2 -----------#
import numpy as np

powers_list = []
#Each game we need to get the id (split left of colon)
for game in data:
    game_id = game.split(":")[0].split()[1]
    game_results = game.split(": ")[1].split("; ")
    #reset colour maxes to 0 when we start a new game
    colour_maxes = {"red":0,"blue":0,"green":0}

    for set in game_results:
        single_choices = set.split(", ")
        for choice in single_choices:
            number = int(choice.split()[0])
            colour = choice.split()[1]
            colour_maxes[colour] = max(colour_maxes[colour],number)
                
    powers_list.append(np.prod(list(colour_maxes.values())))

power_sum = sum(powers_list)

print("Part 2 answer is:",power_sum)