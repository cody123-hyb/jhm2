size = int(input("Input Addition Table Size smaller 10: "))
print("------------------------------------------------------------")

for b in range(1 , size + 1):
    d = [f"{b} + {c} = {b + c}" for c in range(size + 1) if c != 0]
    print("".join([f"{entry:<11}" for entry in d]))

print("------------------------------------------------------------")

