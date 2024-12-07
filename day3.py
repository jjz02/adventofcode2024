import re

data = []

def addData(file):
    with open (file, "r") as f:
        for line in f:
            pattern = r"(do\(\)|don't\(\)|mul\(\d+,\d+\))"
            matches = re.findall(pattern, line)
            data.extend(matches)

addData("day3input.txt")

numbers = []

calculating = True

pattern = r"mul\((\d+),(\d+)\)" 
result = 0

for i in data:
    if i == "don't()":
        calculating = False
        continue
    elif i == "do()":
        calculating = True
        continue
    if calculating:
        matches = re.match(pattern, i)
        if matches:
            x, y = map(int, matches.groups())
            result += x * y

print(result)

