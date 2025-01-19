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
max_number = number [0]
for num in number : 
        if a and b and c and d < max_numfber :
                max_number = num
print("The taller student is", max_number)