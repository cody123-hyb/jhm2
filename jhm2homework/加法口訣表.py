size = int(input("Input Addition Table Size (smaller than 10): "))

print("------------------------------------------------------------")
    
    for b in range(size + 1):
        a = []
        for c in range(size + 1):
            a.append(f"{b} + {c} = {b + c:<5}")
        
        print(" ".join(a))
    
    print("------------------------------------------------------------")

