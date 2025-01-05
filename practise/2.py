import pandas as pd

date = input("Date: ")
category = input("Category: ")
amount = input("Amount: ")
type = input("Type: ")

Data = (date, category, amount, type)

print(Data)

df = pd.read_csv('expenses.csv')
print(df)