import pandas as pd

while True:
    print("1. 新增交易") 
    print("2. 編輯交易") 
    print("3. 刪除交易") 
    print("4. 查看摘要")
    print("5. 儲存並退出")

    a = input("Enter your choice: ")
    print(a)
    if a == '1': 
        date = input("Enter the date: ") 
        category = input("Enter the category: ") 
        amount = input("Enter the amount: ") 
        type_ = input("Enter the type: ") 
        Data = (date, category, amount, type_) 
        print(Data)
        df = pd.read_csv('expenses.csv')

    if not os.path.exists('expenses.csv'):
        df = pd.DataFrame(columns=columns)
        print("無現有檔案，建立新資料表")
        print(df)
        print("Data saved to expenses.csv.")