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
            return False

        # Check if increasing or decreasing
        if (level_1 < level_2) != should_increase:
            return False

    return True


# Stage to count safe reports
def count_safe_reports(reports):
    return sum(1 for report in reports if check_report_safety(report))


# Pipeline execution chain
pipeline = compose(
    count_safe_reports,
    transform,
    extract
)

# Execute the pipeline
safe_reports = pipeline(FILE_PATH)
print(safe_reports)
