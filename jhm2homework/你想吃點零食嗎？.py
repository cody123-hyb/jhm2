first_question = input("Do you want some snacks (yes/no): ")
second_question = input("Enter your choice (ice-cream / cookies / candies ): ")

a=int(second_question)
if first_question.lower() == "no" : 
    print("Good! Let's play games instead.")             

elif first_question.lower() == "yes" : 
    input(a)
    
    if (a) == "ice-cream" :
        print("Remeber to wash your hands.")
    
    elif (a) == "cookies" :
        print("Can you share with your friends？")
    
    elif (a) == "candies" :
        print("Don't eat too much.")
