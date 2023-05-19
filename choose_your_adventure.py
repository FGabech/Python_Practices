name = input("Type your name: ")
print("Welcome", name, "to this adventure!")

answer = input("You are on a dirt road, it has come to an end and you can go left or right. Which way would you like to go? ").lower()

if answer == "left":
    answer2 = input("You come to a river and you can walk around it or swim across it. Type walk to walk around it or swim to swim across it: ").lower()

    if answer2 == "swim":
        print("You swam across and were eaten by something evil under the water.")
        quit()
    elif answer2 == "walk":
        answer3 = input("You walked for many kilometers, and still did not find a way through and start to starve, type fishing if you want to fishing in the river or type hunt if you want to hunt in the woods: ").lower()

        if answer3 == "fishing":
            print("You waited for hours and did not find a fish and starve to death. You lose.")
            quit()
        elif answer3 == "hunt":
            print("You find a trail in the woods and start to follow it, all of a sudden you find yourself facing a grizzly bear, you tried to kill him with bear hands and died. You lose.")
            quit()
        else:
            print('Not a valid option. You lose.')
            quit()
    else:
        print('Not a valid option. You lose.')
        quit()
elif answer == "right":
    answer4 = input("You walk quite a few kilometers and arrive at a a mountain, type climb if you want to climb it or walk if you want to walk through it: ").lower()

    if answer4 == "climb":
        print("You tryed to climb it, but the mountain was very slippery and you fall and died. You lose.")
        quit()
    elif answer4 == "walk":
        answer5 = input("You walked for many hours until you found fruits in some bushes, you are starving. Type yes if you want to eat them or type no if you don't want to eat them: ").lower()

        if answer5 == "no":
            print("You keep walking until you fainted. You lose.")
            quit()
        elif answer5 == "yes":
            print("You ate a lot of fruits and keep some for the way. You keep walking until you find a trail in the woods and start to follow it, until you reached a village. You win!")
            quit()
        else:
            print('Not a valid option. You lose.')
            quit()
    else:
        print('Not a valid option. You lose.')
        quit()
else:
    print('Not a valid option. You lose.')
    quit()

