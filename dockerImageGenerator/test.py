import csv

# print "HelloWorld"
with open("mycsv.csv", "rb") as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        print row