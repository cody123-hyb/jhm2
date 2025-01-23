Sizea = int(input("Input Addition Table Size smaller 10: "))
a = Sizea
print("Addition Table")

for i in range (1 , a + 1):
    for j in (1 , a + 1):
        print(f'{i} + {j}={i + j}', end ='/t')
    print( )

  