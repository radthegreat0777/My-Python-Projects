print("Welcome to my Quiz Phobia")

guess = input("Do you Want to guess and play? ").lower()
count = 0
incorrect = 0

if guess == "yes":
    print(
    """
    Let's Start the Game 
    You Need to Answer 5 Questions
    Score 4 or more to win
    """)
    
    question1 = input("Q1: Which animal is known as the 'Ship of the Desert'?: ").lower()

    if question1 == "camel":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        incorrect += 1

    question2 = input("Q2: How many da are there in a week?: ").lower()

    if question2 == "7" or question2 == "seven" or question2 == "7 days" or question2 == "seven days":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        incorrect += 1

    question3 = input("Q3: How many hours are there in a day?: ").lower()

    if question3 == "24" or question3 == "twenty four" or question3 == "24 hours" or question3 == "twenty four hours":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        incorrect += 1

    question4 = input("Q4: Which animal is known as the king of the jungle?: ").lower()

    if question4 == "lion":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        incorrect += 1

    question5 = input("Q5: Name the National bird of India?: ").lower()

    if question5 == "peacock" or question5 == "the peacock":
        print("Correct....")
        count += 1
    else:
        print("!! Wrong !!")
        incorrect += 1

    if count >= 4:
        print(f"Congrats YOU WIN !!\nYour score is: {count}")
    else:
        print(f"Better Luck Next Time !!\nYour score is {count}")

elif guess == "no":
    print("Thank You for Visiting")

else:
    print("Invalid Input")