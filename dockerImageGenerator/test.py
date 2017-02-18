# Where students do their assignments based on the original csv file.
import csv

# print "HelloWorld"
with open("mycsv.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row
