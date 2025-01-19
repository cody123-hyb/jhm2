time = 0
while time < 4 :
 a = int(input("Input the height of a student 1 in cm: "))
 if a < 0: 
        print("Height must be positive.") 
 elif a > 200: 
        print("Height is greater than 200cm.") 
 else:
    time +=1
    b = int(input("Input the height of a student 2 in cm: "))
    if b < 0: 
            print("Height must be positive.") 
    elif b > 200: 
            print("Height is greater than 200cm.") 
    else:
        time +=1
        c = int(input("Input the height of a student 3 in cm: "))
        if c < 0: 
                print("Height must be positive.") 
        elif c > 200: 
                print("Height is greater than 200cm.") 
        else:
            time +=1
            d = int(input("Input the height of a student 4 in cm: "))
            if d < 0: 
                    print("Height must be positive.") 
            elif d > 200: 
                    print("Height is greater than 200cm.")  
                    time +=1           
        break
print("End of Input")
number = [a,b,c,d]
sma_number = number [0]
for num in number : 
        if num < sma_number :
                sma_number = num
print("The average height of these students is",f'{sma_number:.2f}'" cm.")
lar_number = number [0]
for num in number : 
        if num > lar_number :
                lar_number = num
print("The maximum height of these students is",f'{lar_number:.2f}'" cm.")     
    