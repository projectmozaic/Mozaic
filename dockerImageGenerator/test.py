# Where students do their assignments based on the original csv file.
import csv

# read the csv file and print out each line (basic operation, allows students doing their calculations)
with open("mycsv.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
