data = []

def addData(file):
    with open (file, "r") as file:
        for line in file:
            values = list(map(int, line.split()))
            data.append(values)

addData("day1input.txt")

columns = list(zip(*data))

column1 = sorted(list(columns[0]), reverse=False)
column2 = sorted(list(columns[1]), reverse=False)

tally = 0

for i in range(len(column1)):
    if column1[i]:
        count = column2.count(column1[i])
        result = column1[i] * count 
        tally += result


print(tally)
