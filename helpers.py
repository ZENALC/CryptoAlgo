import logging
import time
import os
from datetime import datetime


def easter_egg():
    import random
    number = random.randint(1, 16)
    sleepTime = 0.25

    if number == 1:
        print('The two most important days in your life are the day you are born and the day you find out why.')
    elif number == 2:
        print('Financial freedom by sacrificing relationships; is it ever worth it?')
    elif number == 3:
        print("A guy asks a woman to sleep with him for $100, and the woman starts thinking. Suddenly the guy says "
              "I'll give you $20 for a night, and the girl gets mad and yells what type of girl do you think I am? "
              "The guy then says that he thought they already established that, and that now they're negotiating.")
    elif number == 4:
        print("We all do dumb things, that's what makes us human.")
    elif number == 5:
        print("Friends are like coins. You rather have 4 quarters than a 100 pennies.")
    elif number == 6:
        print('Fuck Bill Gates')
    elif number == 7:
        print('What is privacy again?')
    elif number == 8:
        print("If the virus was real and super contagious, why didn't it spread during BLM protests?")
    elif number == 9:
        print('Insanity is doing the same shit over and over again. Expecting shit to change.')
    elif number == 10:
        print("Rush B P90 no stop.")
    elif number == 11:
        print('Wakanda forever.')
    elif number == 12:
        print('Read the manuals. Read the books.')
    elif number == 13:
        print('4 cases in New Zealand? Lock down everything again!')
    elif number == 14:
        print('Fake pandemic.')
    elif number == 15:
        print('You think money is a powerful tool? Fuck that, fear will always fuck you up.')
    else:
        print("Fucking shape shifting reptilians, bro. Fucking causing this virus and shit.")

    time.sleep(sleepTime)


def initialize_logger():
    """Initializes logger"""
    if not os.path.exists('Logs'):
        os.mkdir('Logs')

    previousPath = os.getcwd()
    os.chdir('Logs')

    todayDate = datetime.today().strftime('%Y-%m-%d')

    if not os.path.exists(todayDate):
        os.mkdir(todayDate)

    os.chdir(previousPath)

    logFileName = f'{datetime.now().strftime("%H-%M-%S")}.log'
    logging.basicConfig(filename=f'Logs/{todayDate}/{logFileName}', level=logging.INFO, format='%(message)s')
