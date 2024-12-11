# 1.py
from toolz import compose

FILE_PATH = 'assets/input.txt'


# Read the file and split it into lines
def extract(file_path):
    with open(file_path) as file:
        return file.readlines()


# Convert each line into a list
def transform(data):
    return [[int(number) for number in line.strip().split()] for line in data]


# Check if a single report is safe or unsafe
def check_report_safety(report):
    should_increase = report[0] < report[1]

    # Always check the next pair of levels in the report
    for i in range(len(report) - 1):
        level_1 = report[i]
        level_2 = report[i + 1]

        # Check for allowed level difference
        if not (1 <= abs(level_1 - level_2) <= 3):
            return False, i

        # Check if increasing or decreasing
        if (level_1 < level_2) != should_increase:
            return False, i

    return True, -1

# Stage to count safe reports with problem dampener
def count_safe_reports(reports):
    total = 0

    for report in reports:
        is_safe, unsafe_level_index = check_report_safety(report)

        if is_safe:
            total += 1
        else:
            report_copy_1 = report.copy()
            report_copy_1.pop(unsafe_level_index)
            is_safe_1, _ = check_report_safety(report_copy_1)

            if is_safe_1:
                total += 1
                continue

            report_copy_2 = report.copy()
            report_copy_2.pop(unsafe_level_index + 1)
            is_safe_2, _ = check_report_safety(report_copy_2)

            if is_safe_2:
                total += 1

    return total


# Pipeline execution chain
pipeline = compose(
    count_safe_reports,
    transform,
    extract
)

# Execute the pipeline
safe_reports = pipeline(FILE_PATH)
print('Total safe reports:', safe_reports)
