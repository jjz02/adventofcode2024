import numpy as np

data = []

def addData(file):
    with open (file, "r") as file:
        for line in file:
            values = list(map(int, line.split()))
            data.append(values)

addData("day2input.txt")


def checkSuccessReports(row):
        difference_of_row = np.diff(row)

        if all(0 < abs(i) < 4 for i in difference_of_row):
            if all(i > 0 for i in difference_of_row) or all(i < 0 for i in difference_of_row):
                return True

tally = 0

for row in data:
    if checkSuccessReports(row):
        tally+=1
    else:
        for i in range(len(row)):
            modified_row = row[:i] + row[i+1:]

            if checkSuccessReports(modified_row):
                tally += 1
                break

print(tally)