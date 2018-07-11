#!/usr/bin/python

import csv

filename = "test.csv"

# write data to csv file
header = ["COL1", "COL2", "COL3", "COL4"]
data = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
with open(filename, "w") as f:
    writer = csv.writer(f)
    writer.writerows([header])
    writer.writerows(data)

print("write csv: header {}".format(header))
print("write csv: data   {}".format(data))


# read data from csv
header = None
data = []
with open(filename) as csvfile:
    csv_reader = csv.reader(csvfile)
    header = next(csv_reader)
    for row in csv_reader:
        data.append(row)

data = [[int(x) for x in row] for row in data]

print("read csv: header {}".format(header))
print("read csv: data   {}".format(data))
