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

#Step 3:Access specific columns
print("\nAccess the 'Name' column:")
print(df['Name'])

