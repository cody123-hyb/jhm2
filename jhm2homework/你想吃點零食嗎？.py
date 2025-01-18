first_question = input("Do you want some snacks? (yes/no): ").lower()
if first_question == "no":
    print("Good! Let's play games instead.")

elif first_question == "yes":
    second_question = input("Enter your choice (ice-cream / cookies / candies): ").lower()
    
    if second_question == "ice-cream":
        print("Remember to wash your hands.")

    elif second_question == "cookies":
        print("Can you share with your friends?")
    
    elif second_question == "candies":
        print("Don't eat too much.")
