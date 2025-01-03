import pandas as pd

#Step 1:Create DataFrame
data ={
    'Name':['Alice','Bob','Charlie'],
    'Age':[25,30,35],
    'City':['New York','Los Angeles','Chicago']
}
df  =pd.DataFrame(data)

#Step 2:Display the DataFrame
print("Original DataFrame:")
print(df)


df = pd.DataFrame(my_dict)

print(df)

print(df['Name'])

print(df.iloc[1])

df['Salary'] = [70000, 80000, 75000]
print(df)

filtered_df = df[df['Age'] > 28]
print(filtered_df)

average_salary = df['Salary'].mean()
