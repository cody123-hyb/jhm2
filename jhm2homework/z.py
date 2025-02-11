size = int(input("請輸入加法口訣表大小（小於 10 的正整數）："))

# 列印加法口訣表
for i in range(size + 1):
    row = [f"{i} + {j} = {i + j}" for j in range(size + 1)]
    # 根據和的大小調整空格
    formatted_row = [f"{entry:<10}" for entry in row]  # 每個條目寬度設置為10
    print("".join(formatted_row))