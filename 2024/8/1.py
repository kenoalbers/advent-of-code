# 1.py
import numpy as np

FILE_PATH = 'assets/input.txt'


# Read the file and split it into lines
def extract(file_path):
    with open(file_path) as file:
        return file.readlines()


# Split data into a grid
def transform(data):
    return [[letter for letter in line.strip()] for line in data]


# Check and categorize antennas with coordinates
def create_antenna_list(raw_antenna_map):
    antenna_list = []

    for i, line in enumerate(raw_antenna_map):
        for j, letter in enumerate(line):
            if letter != '.':
                antenna_list.append([letter, (int(j), int(i))])

    return antenna_list


# Calculate a list of all possible antinodes
def create_antinode_list(antenna_list):
    antinode_list = []

    for antenna in antenna_list:
        for other_antenna in antenna_list:
            # Ignore if exact same antenna
            if antenna[1] == other_antenna[1]:
                continue

            # Check if the same antenna referenced
            if antenna[0] == other_antenna[0]:
                # Calculate distance
                distance = (np.array(other_antenna[1] - np.array(antenna[1])))
                # Scale vector by 2
                distance *= 2
                # Add to antenna
                distance += np.array(antenna[1])
            else:
                continue

            # Add to antinode_list if not already in there
            distance_tuple = tuple(distance)

            if distance_tuple not in antinode_list:
                antinode_list.append(distance_tuple)

    return antinode_list


# Check if a value is inside a specified boundary of any 2D array.
def check_if_in_boundary(x_length, y_length, x, y):
    if not (0 <= x < x_length):
        return False
    if not (0 <= y < y_length):
        return False
    return True


# Check for every antinode in list if in boundary
def check_antinodes_if_in_boundary(raw_antenna_map, antinode_list):
    return [antinode for antinode in antinode_list
            if check_if_in_boundary(len(raw_antenna_map[0]), len(raw_antenna_map), antinode[0], antinode[1])]


# Execution chain
my_antenna_map = transform(extract(FILE_PATH))
my_antenna_list = create_antenna_list(my_antenna_map)
my_antinode_list = create_antinode_list(my_antenna_list)
my_antinode_list_in_boundary = check_antinodes_if_in_boundary(my_antenna_map, my_antinode_list)
print('Number of unique antinodes:', len(my_antinode_list_in_boundary))
