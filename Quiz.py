#Python quiz game

questions = ("1.How many bones are there in human body?",
             "2.Which planet is the hottest one in the universe?",
             "3.Who is Superstar of tollywood film industry?",
             "4.Who plays Lord Rama role in the upcoming ramayana movie?",
             "5.Which animal lays the largest eggs?",
             "6.Which team won IPL 2025?",
             "7.Which indian film has the record of highest collection gross till now?"
             )

options = (("A.207","B.206","C.210","D.205"),
           ("A.Mars","B.Venus","C.Jupiter", "D.Mercury"),
           ("A.Allu arjun","B.Prabhas","C.Mahesh babu","D.NTR"),
           ("A.Ranveer","B.Ranbir", "C.Hritik", "D.Mahesh babu"),
           ("A.Hen","B.Girraffe","C.Ostrich","D.Eagle"),
           ("A.CSK","B.MI","C.LSG","D.RCB"),
           ("A.Dangal","B.Baahubali 2","C.RRR","D.KGF2"))

answers = ("B","B","C","B","C","D","A")
question_num = 0
score = 0
guesses = []

print("LET'S START THE QUIZ")
for question in questions:
    print(question)
    for option in options[question_num]:
        print(option )
    guess = input("Enter the answer you think(A,B,C,B):").upper()
    guesses .append(guess)
    if guess == answers[question_num]:
        score += 1
        print("Correct answer....yay")
    else:
        print("Incorrect...Better luck next time..")
        print(f"{answers[question_num]} is the correct answer") 


    question_num += 1


print("-----------------")
print("      RESULT     ")
print("-----------------")
print("The correct options are")
for answer in answers:
    print(answer, end=" ")
print()
print("Your choosen options are")
for guess in guesses:
    print(guess, end=" ")
print()

score = int(score/len(questions)*100)
print(f"You scored {score}%....")
