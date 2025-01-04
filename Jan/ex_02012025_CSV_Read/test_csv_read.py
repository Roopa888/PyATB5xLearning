import pandas as pd
import csv
# reading using csv not pandas
class Test_Read():
    def test_read_csv(self):
            with open('userdata.csv') as csvfile:
                reader=csv.reader(csvfile)
                for row in reader:
                    print(row[0],row[1])

    def test_read_pandas(self):
         ds=pd.read_csv('userdata.csv')
         print(ds)