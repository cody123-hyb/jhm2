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




