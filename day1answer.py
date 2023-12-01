#Point to input data location
input_file = r"C:\Users\thompsow0570\OneDrive - ARCADIS\Documents\Repositories\AdventOfCode2023\Inputs\day1.txt"

#Read input data file
with open(input_file) as file:
    data = [line.rstrip() for line in file]

#Initiate lists
calibration_values = []
line_int_list = []
int_in_line = []

#--------- Part 1 ----------#
#Read data line by line and convert numbers to integers, skipping the strings (letters)
for line in data:
    int_in_line = []

    for char in line:
        try:
            char = int(char)
            int_in_line.append(char)
        except:
            pass

    line_int_list.append(int_in_line)   #each line, spit back the result to the master list     

#Take only the first and last digit of each line, concatenate them, and report back to master list
for line in line_int_list:
    first_digit = line[0]
    last_digit = line[-1]

    calibration_values.append(int(str(first_digit)+str(last_digit)))

###### Sum of all calibration values #####
calib_sum = sum(calibration_values)
print(calib_sum)

#--------- Part 2 ---------#

numbermap = {"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7","eight":"8","nine":"9"}

#Initiate lists
calibration_values = []
line_int_list = []
int_in_line = []

#Read data line by line
for line in data:
    int_in_line = []
    #Find all the substrings corresponding to numbers and store them in a replacements list. This is very important for cases like "eightwo" and "oneight".
    replacements_list = []
    for number in numbermap:
        if line.lower().find(number) != -1:
            replacements_list.append([number,line.lower().find(number)])

    #Do the same using rfind for the right hand values (if any)
    for number in numbermap:
        if line.lower().rfind(number) != -1:
            replacements_list.append([number,line.lower().rfind(number)])
    
    #Go through all the replacements necessary
    replacement_count = 0
    for item in replacements_list:
        line = line[:item[1]+replacement_count] + numbermap.get(item[0]) + line[item[1]+replacement_count:]
        replacement_count+=1
    #Same process as part 1
    for char in line:
        try:
            char = int(char)
            int_in_line.append(char)
        except:
            pass

    line_int_list.append(int_in_line)   #each line, spit back the result to the master list

#Take only the first and last digit of each line, concatenate them, and report back to master list
for line in line_int_list:
    first_digit = line[0]
    last_digit = line[-1]

    calibration_values.append(int(str(first_digit)+str(last_digit)))

###### Sum of all calibration values #####
calib_sum = sum(calibration_values)
print(calib_sum)


