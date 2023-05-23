import random



def roll_dice():

    dice_drawing = {
        1:(
            "____________",
            "|           |",
            "|     1     |",
            "|     0     |",
            "|           |",
            "|___________|",
        ),
        2:(
            "____________",
            "|           |",
            "|  0        |",
            "|     2     |",
            "|        0  |",
            "|___________|",
        ),
        3:(
            "____________",
            "|           |",
            "|  0  3     |",
            "|     0     |",
            "|        0  |",
            "|___________|",
        ),
        4:(
            "____________",
            "|           |",
            "|  0     0  |",
            "|     4     |",
            "|  0     0  |",
            "|___________|",
        ),
        5:(
            "____________",
            "|           |",
            "|  0  5 0   |",
            "|     0     |",
            "|  0    0   |",
            "|___________|",
        ),
        6:(
            "____________",
            "|           |",
            "|  0     0  |",
            "|  0  6  0  |",
            "|  0     0  |",
            "|___________|",
        ),
    }

    play = input("Do you want to roll the dice? (Yes/No) ").lower()
    
    while play == "yes":
        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)

        print("Dice rolled: {} and {}".format(dice1, dice2))
        print("\n".join(dice_drawing[dice1]))
        print("\n".join(dice_drawing[dice2]))

        play = input("Do you want to roll the dice again? (Yes/No) \n").lower()


roll_dice()
