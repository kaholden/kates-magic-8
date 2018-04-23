from random import randint
from time import sleep

magic8_answers = ['It is certain', 'Without a doubt', 'You may rely on it',
                  'Most likely', 'Outlook good', 'Yes', 'Ask again later',
                  'Reply hazy, try again later', 'Better not tell you now',
                  'Don\'t count on it', 'My reply is no', 'Outlook not good',
                  'Very doubtful', 'No', 'My sources say no']

def magic8_shake():
    game_active = True
    while game_active:
        rand_answers = randint(0, 14)
        input("What yes/no question do you want the answer to? \n")
        print("Hmmmmmm.... good question ...")
        sleep(2)
        print(magic8_answers[rand_answers])
        user_input = input("Would you like to ask another question (y/n)?\n")
        user_input = user_input.lower()
        if user_input == 'n':
            game_active = False

print("Welcome to Kate's Magic 8! Please ask a yes/no question to find your answer.")

magic8_shake()
