import re
import numpy as np

#Point to input data location
input_file = r"C:\Users\walte\Documents\GitHub\AdventOfCode2023\Inputs\day3.txt"

#Read input data file
with open(input_file) as file:
    data = [line.rstrip() for line in file]

#------------ PART 1 -----------#
#test data
#data =  ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]

number_matches = []
#dot_matches = []
symbol_matches = []
symbol_match_rows = []
number_match_rows = []

trigger_zones = np.zeros((len(data),len(data[0])),np.int8)

valid_nums = []

#first, let's find the symbols and numbers
row_counter = 0
for row in data:
    #Find symbols
    for match in re.finditer(r"[^0-9.]+",row):
        symbol_match_rows.append(row_counter)
        symbol_matches.append(match)
    
    #Find numbers
    for match in re.finditer(r"\d+",row):
        number_match_rows.append(row_counter)
        number_matches.append(match)

    row_counter+=1

#build trigger zones in 3x3 grid around symbols
for i in range(len(symbol_matches)):
    column = symbol_matches[i].span()[0]
    row = symbol_match_rows[i]
    #set trigger zones to 1 around symbols
    trigger_zones[row-1:row+2,column-1:column+2] = 1


#iterate through number matches and check if any point of them lies in the trigger zone
for i in range(len(number_matches)):
    row = number_match_rows[i]
    span_start = number_matches[i].span()[0]
    span_end = number_matches[i].span()[1]-1
    number = int(number_matches[i][0])
    #Do the check
    if trigger_zones[row,span_start] == 1 or trigger_zones[row,span_end] == 1:
        valid_nums.append(number)

#Part 1 Answer
answer = sum(valid_nums)
print("Part 1 answer is:",answer)

#-------------PART 2----------------#
#test data
#data =  ["467..114..","...*......","..35..633.","......#...","617*......",".....+.58.","..592.....","......755.","...$.*....",".664.598.."]

number_matches = []
symbol_matches = []
symbol_match_rows = []
number_match_rows = []

gear_ratios = []

#first, let's find the symbols and numbers
row_counter = 0
for row in data:
    #Find symbols
    for match in re.finditer(r"\*",row):
        symbol_match_rows.append(row_counter)
        symbol_matches.append(match)
    
    #Find numbers
    for match in re.finditer(r"\d+",row):
        number_match_rows.append(row_counter)
        number_matches.append(match)

    row_counter+=1

#Belt and braces approach... do it one * at a time.

#build trigger zones in 3x3 grid around symbols
for i in range(len(symbol_matches)):
    #initialise trigger_zones fresh each time
    trigger_zones = np.zeros((len(data),len(data[0])),np.int8)
    potential_ratios = []

    column = symbol_matches[i].span()[0]
    row = symbol_match_rows[i]
    #set trigger zones to 1 around symbols ONE AT A TIME, as we are in the for loop
    trigger_zones[row-1:row+2,column-1:column+2] = 1
    #iterate through number matches and check if any point of them lies in the trigger zone
    for i in range(len(number_matches)):
        row = number_match_rows[i]
        span_start = number_matches[i].span()[0]
        span_end = number_matches[i].span()[1]-1
        number = int(number_matches[i][0])
        #Do the check
        if trigger_zones[row,span_start] == 1 or trigger_zones[row,span_end] == 1:
            potential_ratios.append(number)
    
    if len(potential_ratios) == 2:
        gear_ratios.append(potential_ratios[0]*potential_ratios[1])
    

#Part 2 Answer
answer = sum(gear_ratios)
print("Part 2 answer is:",answer)