def replace_word():

    print("Hello and welcome to word replacement app: ")
    str = "Hi guys, I am Felippe!"
    print(str)
    
    word_to_replace = input("Enter the word to replace: ")
    word_replacement = input("Enter the word replacement: ")

    print(str.replace(word_to_replace, word_replacement))

replace_word()