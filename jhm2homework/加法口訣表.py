size = int(input("Input Addition Table Size smaller 10："))

print("------------------------------------------------------------")

for b in range(size + 1):
    for c in range(size + 1):
        a = [f"{b} + {c} = {b + c}{'  ' if b + c < 10 else ' '}" for j in range(1)]
    formatted_a = [f"{entry:<11}" for entry in a]
        
        
    print("".join(formatted_a))
    
print("------------------------------------------------------------")


