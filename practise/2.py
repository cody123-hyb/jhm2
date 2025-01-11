import pandas as pd
import os

# 定義資料表的欄位名稱
columns = ['Date', 'Category', 'Amount', 'Type']

# 嘗試從檔案載入資料
file_name = 'transactions.csv'
if os.path.exists(file_name):
    df = pd.read_csv(file_name)
    print("資料表已成功載入。")
else:
    df = pd.DataFrame(columns=columns)
    print("檔案不存在，已建立空資料表。")

# 功能選項
def display_menu():
    print("\n請選擇功能選項：")
    print("1. 新增交易")
    print("2. 編輯交易")
    print("3. 刪除交易")
    print("4. 查看摘要")
    print("5. 儲存並退出")

def add_transaction():
    date = input("請輸入日期（YYYY-MM-DD）：")
    category = input("請輸入類別：")
    amount = input("請輸入金額：")
    while not amount.replace('.', '', 1).isdigit():
        amount = input("金額無效，請重新輸入：")
    type_ = input("請輸入類型（收入/支出）：")
    df.loc[len(df)] = [date, category, float(amount), type_]
    print("交易新增成功。")

def edit_transaction():
    index = int(input("請輸入需要編輯的交易索引："))
    if 0 <= index < len(df):
        print(f"當前交易資料：{df.loc[index].to_dict()}")
        date = input("請輸入日期（YYYY-MM-DD）（按 Enter 保留原值）：")
        category = input("請輸入類別（按 Enter 保留原值）：")
        amount = input("請輸入金額（按 Enter 保留原值）：")
        type_ = input("請輸入類型（收入/支出）（按 Enter 保留原值）：")
        if date: df.at[index, 'Date'] = date
        if category: df.at[index, 'Category'] = category
        if amount.replace('.', '', 1).isdigit(): df.at[index, 'Amount'] = float(amount)
        if type_: df.at[index, 'Type'] = type_
        print("交易修改成功。")
    else:
        print("無效的索引。")

def delete_transaction():
    index = int(input("請輸入需要刪除的交易索引："))
    if 0 <= index < len(df):
        df.drop(index, inplace=True)
        df.reset_index(drop=True, inplace=True)
        print("交易刪除成功。")
    else:
        print("無效的索引。")

def view_summary():
    total_expense = df[df['Type'] == '支出']['Amount'].sum()
    total_income = df[df['Type'] == '收入']['Amount'].sum()
    balance = total_income - total_expense
    print(f"\n總支出：{total_expense}")
    print(f"總收入：{total_income}")
    print(f"結餘：{balance}")

while True:
    display_menu()
    choice = input("請輸入功能選項（1-5）：")
    if choice == '1':
        add_transaction()
    elif choice == '2':
        edit_transaction()
    elif choice == '3':
        delete_transaction()
    elif choice == '4':
        view_summary()
    elif choice == '5':
        df.to_csv(file_name, index=False)
        print("資料已儲存。感謝使用！")
        break
    else:
        print("無效的選項，請重試。")
