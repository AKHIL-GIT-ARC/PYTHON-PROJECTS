#Dice rollling program
import random

dice_art = {
    1:("┌───────────┐",
       "│           │",
       "│     ●     │",
       "│           │",
       "└───────────┘"
       ),
       2:("┌───────────┐",
          "│  ●        │",
          "│           │",
          "│       ●   │",
          "└───────────┘"
          ),
          3:("┌───────────┐",
             "│ ●         │",
             "│     ●     │",
             "│         ● │",
             "└───────────┘"
             ),
             4:("┌───────────┐",
                "│ ●       ● │",
                "│           │",
                "│ ●       ● │",
                "└───────────┘"
                ),
                5:("┌───────────┐",
                   "│ ●       ● │",
                   "│     ●     │",
                   "│ ●       ● │",
                   "└───────────┘"
                   ),
                   6:("┌───────────┐",
                      "│ ●   ●   ● │",
                      "│ ●   ●   ● │",
                      "│ ●   ●   ● │",
                      "└───────────┘"
                      )
}
dice = []
total = 0
dice_num = int(input("Enter how many dice you would like to roll:"))
for die in range(dice_num):   
    dice.append(random.randint(1,6))
    print(dice)
# for die in range(dice_num):
#     for line in dice_art.get(dice[die]):
#         print(line)
for line in range(5):
    for die in dice:
        print(dice_art.get(die)[line],end= " ")
    print()
for die in dice:
    total = total + die
print(f"Total is : {total}")
 