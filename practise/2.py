import pandas as pd

while True:
    print("1. 新增交易") 
    print("2. 編輯交易") 
    print("3. 刪除交易") 
    print("4. 查看摘要")
    print("5. 儲存並退出")

    a = input("Enter your choice: ")
    print(a)
    
    
    #新增交易
    if a == '1': 
        date = input("Enter the date (YYYY-MM-DD): ") 
        category = input("Enter the category: ") 
        amount = input("Enter the amount: ") 
        type = input("Enter the type: ") 
        Data = (date,category, amount,type) 
        print(Data)
        df = pd.read_csv('expenses.csv')
    if not os.path.exists('expenses.csv'):

        df = pd.DataFrame(columns=columns)
        print("無現有檔案，建立新資料表")
        print(df)
        print("Data saved to expenses.csv.")
    
    
    #編輯交易
    if a == '2':
        index = int(input("輸入要編輯的交易索引: "))
        print(df.loc[index]) 
        new_date = input("輸入新日期 (Enter 保留原值): ") or df.loc[index, 'Date']
        df.loc[index] = {'Date': new_date, 'Category': new_category, 'Amount': new_amount, 'Type': new_type}
        print("交易更新成功！")
    
    
    #刪除交易
    if a == '3':
        index = int(input("輸入要刪除的交易索引: "))
        df = df.drop(index).reset_index(drop=True)
        print("交易刪除成功！")

    
    #查看摘要
    if a == '4':
        total_expenses = df[df['Type'] == '支出']['Amount'].sum()
        total_income = df[df['Type'] == '收入']['Amount'].sum()
        savings = total_income - total_expenses
        print(f"總支出: {total_expenses}")
        print(f"總收入: {total_income}")
        print(f"結餘: {savings}")
        if total_expenses == 0 and total_income == 0: print("無相關資料")

    #儲存並退出
    if a == '5':
        df.to_csv('expenses.csv', index=False)
        print("資料已儲存！")
        break
        print("程式結束,感謝使用")


