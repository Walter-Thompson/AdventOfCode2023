import numpy as np

#Point to input data location
input_file = r"C:\Users\thompsow0570\OneDrive - ARCADIS\Documents\Repositories\AdventOfCode2023\Inputs\day6.txt"

#Read input data file
with open(input_file) as file:
    data = [line.rstrip() for line in file]

#data =  ['Time:      7  15   30','Distance:  9  40  200']

times = data[0].split(":     ")[1].split()
dists = data[1].split(": ")[1].split()

win_combs = []

for i in range(len(times)):
    race_time = int(times[i])
    race_dist = int(dists[i])

    race_combs = []

    for charge in range(race_time):
        speed = charge
        time = race_time - charge
        dist = speed*time
        if dist > race_dist:
            race_combs.append(dist)

    win_combs.append(len(race_combs))

print("Part 1 answer:", np.prod(win_combs))

#-------------PART 2---------------#

times = data[0].split(":     ")[1].split()
dists = data[1].split(": ")[1].split()

times = int(''.join(times))
dists = int(''.join(dists))

win_combs = []

#find min time to win

for charge in range(times):
    speed = charge
    time = times - charge
    dist = speed*time
    if dist > dists:
        print(charge)
        win_combs.append(charge)
        break

#find max time to win

for charge in range(times,0,-1):
    speed = charge
    time = times - charge
    dist = speed*time
    if dist > dists:
        print(charge)
        win_combs.append(charge)
        break

num_wins = win_combs[1]-win_combs[0]+1    

print("Part 2 answer:", num_wins)