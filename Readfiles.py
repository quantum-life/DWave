# Import Libraries
import csv

# Dictionaries
classification = {}

# Variables
k = 0   # Identification Markers (Time and File Name)
i = -1  # Total rows processed (-1 sets counter to zero)
n = 1   # Row being processed
x = 0   # Spectral Colour
j = 4   # Spectral Intensity

# Definitions
# Time Label            => classification[0]
# File Label            => classification[1]
# time                  => classification[k]
# file name             => classification[k + 1]
# spectrum intensity    => classification[j + 2]
# spectrum colour       => classification[x + 2]


# Setting Locations
imaging_area = '/home/family/Pictures/snow/sky2.csv'     # Location where images are located
csv_file = '/home/family/Pictures/snow/sky.csv'          # location and file name for the csv file

wr_file = open(imaging_area, "w")
lineList = list(csv.reader(open(csv_file, 'r', newline=''), delimiter=','))

for row in lineList:
    for rows in range(0, 6):
        i += 1
        classification[i] = row[rows:][0]
        print(classification[i])

print(classification[0], ',', classification[1], ', value, spectrum', file=wr_file)
print(classification[0], ',', classification[1], ', value, spectrum k n x i j')

while n < (i - 6) / 6 + 1:
    x = 0
    k = n * 6
    n += 1
    j += 2

    while x < 4:
        print(classification[k], ',', classification[k + 1], ',', classification[j + 2], ',', classification[x + 2],
              file=wr_file)
        print(classification[k], ',', classification[k + 1], ',', classification[j + 2], ',', classification[x + 2],
              k, n, x, i, j)
        x += 1
        j += 1
else:
    print('\nImage Processing is Complete')

wr_file.close()
