# import CSV
import csv

with open("TestData.csv", "r") as csvfile:  # better to use "r " mode .W/o "r" also it works though
    reader = csv.reader(csvfile)  # for this reader to call import csv is needed
    for col in reader:
         print(col[0],col[1],sep="|")

    # for row in reader:  # both ways we can get the contents /if we print row that is a list
    #     print(row)
