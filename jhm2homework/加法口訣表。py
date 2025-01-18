# 獲取用戶輸入的口訣表大小
size = int(input("請輸入口訣表大小 (小於 10 的正整數): "))

# 列印加法口訣表
print(f"\n{size} 以內的加法口訣表:")
for i in range(1, size + 1):
    for j in range(1, size + 1):
        result = i + j
        # 當兩個數的和為個位數時，補充兩個空格；當兩個數的和為兩位數時，補充一個空格
        if result < 10:
            print(f"{result}  ", end='')
        else:
            print(f"{result} ", end='')
    print()  # 每一行結束後換行
