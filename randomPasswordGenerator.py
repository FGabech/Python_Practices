import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%¨&*()_-=+§?")

def generate_password():
    password_lenght = int(input("How long do you want your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_lenght):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)

option = input("Do you want to generate a password? (Yes/No) ").lower()

if option == "yes":
    generate_password()
elif option == "no":
    print("Maybe next time! ")
    quit()
else:
    print("Invalid input, please input Yes or No.") 