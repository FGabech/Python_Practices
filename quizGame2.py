print("Welcome to computer quiz game!")

playing = input("Do you wanna play? ")

if playing.lower() != "yes":
    print("Maybe next time! :( ")
    quit() #essa função termina o programa.
else:
    print("Okay! Let's play :) ")

score = 0

quiz = { #dictionary
    "question1": {
        "question": "What does CPU stand for? ",
        "answer": "central processing unit"
    },
    "question2": {
        "question": "What does GPU stand for? ",
        "answer": "graphic processing unit"
    },
    "question3": {
        "question": "What does RAM stand for? ",
        "answer": "random access memory"
    },
    "question4": {
        "question": "What does PSU stand for? ",
        "answer": "power supply"
    },
    "question5": {
        "question": "What is the airspeed velocity of an unladen swallow? ",
        "answer": "african or european"
    },
    "question6": {
        "question": "What is your quest? ",
        "answer": "to seek the holy grail"
    },
}

for key, value in quiz.items():
    print(value['question'])
    answer = input("Your answer is? ").lower()

    if answer == value['answer'].lower():
        print("Correct!")
        score += 1
        print("You got "+ str(score) + " questions correct!", "\n")
    else:
        print("Incorrect!")
        print("The answer is: ", value['answer'], "\n")


print("You got "+ str(int((score/7) * 100)) + "%.")