# install pandas using pip insatll (venv prompt) and then import it and use teh read_csv function of pandas library
import pandas as pd
output=pd.read_csv("TestData.csv")
print(output)

# if we want to print specific columns from pandas data frames /CSV file eg:Only password col below
# columns = ['password']
# output=pd.read_csv("TestData.csv",usecols=columns)
# print(output)