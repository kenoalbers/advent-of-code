# 1.py

FILE_PATH = 'assets/input.txt'

# Read the whole file
def extract(file_path):
    with open(file_path) as file:
        return file.read()


# Convert into a list of stones
def transform(raw_data):
    return [int(number) for number in raw_data.split(' ')]


# Apply rules to a single stone
def apply_rules(stone):
    stones = []

    # Rule 1
    if stone == 0:
        stones.append(1)
        return stones

    # Rule 2
    digits = len(str(stone))
    if (digits % 2) == 0:
        new_stones_digits = int(digits / 2)

        stones.append(int(str(stone)[:new_stones_digits]))
        stones.append(int(str(stone)[new_stones_digits:]))
        return stones

    # Rule 3
    stones.append(stone * 2024)
    return stones


# Apply rules to all stones in a list of stones
def apply_rules_to_all(stones):
    new_stones = []

    for stone in stones:
        new_stones.extend(apply_rules(stone))

    return new_stones


def main():
    data = extract(FILE_PATH)
    stones = transform(data)

    for i in range(0,25):
        stones = apply_rules_to_all(stones)

    print('Number of stones:', len(stones))

main()
