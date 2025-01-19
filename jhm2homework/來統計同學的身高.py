times = 1
number = []

while times < 4 :
    input("Input the height of a student {times} in cm: ")
    if height < 0: 
        print("Height must be positive.") 
    elif height > 200: 
        print("Height is greater than 200cm.") 
    else:
        times += 1

print ("End of Input")




