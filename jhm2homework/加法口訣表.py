size = int(input("請輸入加法口訣表大小（小於 10 的正整數）："))

print("------------------------------------------------------------")

for b in range(size + 1):
    
    a = [f"{b} + {c} = { b + c }" for j in range(size + 1)]

    formatted_a = [f"{entry:<11}" for entry in a]



    print("".join(formatted_a))

print("------------------------------------------------------------")
