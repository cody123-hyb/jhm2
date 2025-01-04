import pandas as pd

Data=(input("Date:") 
      input("Category:")
      input("Amount:")
      input("Type:"))

df = pd.DataFrame(Data)
import os
if os.path.isfile('资料表'):
    df = pd.read_csv('资料表')#, index_col=0)
    print("Data loaded from 资料库.")
    #print(df)
Data = {
    'Date': [], 
    'Category': [],
    'Amount': [],
    'Type': [] 
}
B = input(Data)
while B != "5":
    if B == "1":
        print("Add Transaction")
        C = input("Enter the date (YYYY-MM-DD): ")
        D = input("Enter the category (e.g, Food, Transport): ")
        E = float(input("Enter the amount: "))
        F = input("Enter the type (Expense/Income): ")
        df.loc[len(df.index)] = [C, D, E, F]
        print("Transaction added successfully.")
        #print(df)
    elif B == "2":
        print("Edit Transaction")
        G = int(input("Enter the transaction index to edit: "))
        print("Current transaction details: ")
        print(df.iloc[G])
        C = input("Enter the new date (YYYY-MM-DD) or press Enter to keep current: ")
        D = input("Enter the new category or press Enter to keep current: ")
        H = input("Enter the new amount or press Enter to keep current: ")
        F = input("Enter the new type (Expense/Income) or press Enter to keep current: ")
        if C != "":
            df.loc[G,'Date'] = C
        if D != "":
            df.loc[G,'Category'] = D
        if H != "":
            E = float(H)
            df.loc[G,'Amount'] = E
        if F != "":
            df.loc[G,'Type'] = F
        print("Transaction updated successfully.")
        #print(df)
    elif B == "3":
        print("Delete Transaction")
        G = int(input("Enter the transaction index to delete: "))
        df = df.drop(labels=G)
        print("Transaction deleted successfully.")
        #print(df)
    elif B == "4":
        print("View Summary")
        print("\n--- Expenses Summary ---")
        filtered_df1 = df[df['Type'] == "Expense"]
        summary_df1 = filtered_df1['Amount'].sum()
        print("Total Expenses: ", summary_df1)
        print("\n--- Income Summary ---")
        filtered_df2 = df[df['Type'] == "Income"]
        summary_df2 = filtered_df2['Amount'].sum()
        print("Total Income: ", summary_df2)
        print("\nTotal Savings: ", summary_df2 - summary_df1)
    else:
        print("Try again")

    B = input(A)
df.to_csv('expenses.csv', index=False)
print("Data saved to expenses.csv.")