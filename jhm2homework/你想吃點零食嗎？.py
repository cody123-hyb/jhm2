first_question = input("Do you want some snacks (yes/no): ")
second_question = input("Enter your choice (ice-cream / cookies / candies ): ")

a = int(first_question)
b = int(second_question)

if a == "yes" :
    input(second_question)
    
    if b == "ice cream" :
        print("Remeber to wash your hands.")
    
    if b == "cookies" :
        print("Can you share with your friends？")
    
    if b == "candies" :
        print("Don't eat too much.")

if a == "no" : 
    print("Good! Let's play games instead.")                


    


