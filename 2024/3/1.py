# 1.py
import re

print(sum(int(x) * int(y) for x, y in re.findall(r'mul\(?(\d{1,3}),?(\d{1,3})\)', open('assets/input.txt').read())))
