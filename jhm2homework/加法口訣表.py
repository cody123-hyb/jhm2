Sizea = int(input("Input Addition Table Size smaller 10: "))
a = Sizea
print("Addition Table")

for i in range (1 , a + 1):
    for j in (1 , a + 1):
        cs = j + i
        if cs < 10:
            print(f'{} + {i} = {cs}', end ='  ')
        else: 
            print(f'{} + {i} = {cs}', end =' ')   
    print( )

  