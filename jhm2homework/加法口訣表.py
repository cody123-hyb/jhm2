Sizea = int(input("Input Addition Table Size smaller 10: "))
a = Sizea
print("Addition Table")

print("------------------------------------------------------------")


for i in range (1 , a + 1):
    for j in (1 , a + 1):
        cs = i + j

        if cs < 10:
            print(f'{i} + {j} = {cs}', end ='  ')
        else: 
            print(f'{i} + {j} = {cs}', end =' ')   
    print( )

print("------------------------------------------------------------")