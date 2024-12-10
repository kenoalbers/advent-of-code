# 1.py

# Open file and extract contents
with open('assets/input_demo.txt') as file:
    data = [line.split() for line in file]

# Sort contents into two lists
myList1 = sorted([int(line[0]) for line in data])
myList2 = sorted([int(line[1]) for line in data])

# Calculate the total distance
total_distance = sum(abs(myList1[i] - myList2[i]) for i in range(len(myList1)))

print('Total distance:', total_distance)
