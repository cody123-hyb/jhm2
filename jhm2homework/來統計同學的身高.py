numbera = input ("Input the height of a student 1 in cm: ")
numberb = input ("Input the height of a student 2 in cm: ")
numberc = input ("Input the height of a student 3 in cm: ")
numberd = input ("Input the height of a student 4 in cm: ")
if numbera and numberb and numberc and numberd < 0 :
    print("Height must be positive.")

elif numbera and numberb and numberc and numberd > 200 :
    print("Height is greater than 200cm.")


