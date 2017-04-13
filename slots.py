### Grapes = u"\U0001F347"
### Cherries = u"\U0001F352"
### Lemon = u"\U0001F34B"
### Bell = u"\U0001F514"
### Fire = u"\U0001F525"

import random
import time
from decimal import Decimal

wallet = Decimal('100.00')
wager = 0

reel_1 = 0
reel_2 = 0
reel_3 = 0

def bet():
    global wallet
    global wager
    if wallet <= 0:
        print("You're out of money! See you next time!")
        quit()
    else:
        print("You have $" + str(wallet) + " to play with.")
        wager = Decimal(input("Place a bet between .25 and 100.00 $"))
        if wager > wallet:
            print("You don't have enough money! Enter a bet less than $" + str(wallet))
            bet()
        else:
            spin()

def spin():
    global reel_1
    global reel_2
    global reel_3
    print("Spinning...")
    time.sleep(1)
    reel_1 = random.randrange(1, 11)
    reel_2 = random.randrange(1, 11)
    reel_3 = random.randrange(1, 11)
    if reel_1 >= 1 and reel_1 <= 3:
    ### result is cherries
      reel_1 = u"\U0001F352"
    elif reel_1 >= 4 and reel_1 <= 6:
    ### result is grapes
        reel_1 = u"\U0001F347"
    elif reel_1 >= 6 and reel_1 <= 8:
    ### result is bell
        reel_1 = u"\U0001F514"
    elif reel_1 >= 9:
    ### result is fire
        reel_1 = u"\U0001F525"

    if reel_2 >= 1 and reel_2 <= 3:
      reel_2 = u"\U0001F352"
    elif reel_2 == 4 or reel_2 == 5:
        ### result is grapes
        reel_2 = u"\U0001F347"
    elif reel_2 == 6 or reel_2 == 7:
        ### result is bell
        reel_2 = u"\U0001F514"
    elif reel_2 == 8:
        ### result is fire
       reel_2 = u"\U0001F525"
    elif reel_2 >= 9:
        ### result is lemon
       reel_2 = u"\U0001F34B"

    if reel_3 >= 1 and reel_3 <= 2:
        ### result is grapes
        reel_3 = u"\U0001F347"
    elif reel_3 == 3 or reel_3 == 4:
        reel_3 = u"\U0001F514"
    elif reel_3 == 5 or reel_3 == 6:
       reel_3 = u"\U0001F525"
    elif reel_3 >= 7:
        ### result is lemon
       reel_3 = u"\U0001F34B"

    result()

def result():
    global wallet
    global wager
    print('|  ' + reel_1 + '   |  ' + reel_2 + '   |  ' + reel_3 + '  |')
    if reel_1 == u"\U0001F352" and reel_2 == u"\U0001F352":
        wallet += (wager * 2)
        print("You won $" + str(wager * 2))
    elif reel_1 == u"\U0001F352":
        print("You won even money!")
    elif reel_1 == u"\U0001F347" and reel_2 == u"\U0001F347" and reel_3 == u"\U0001F347":
        wallet += (wager * 4) 
        print("You have won $" + str(wager * 4))
    elif reel_1 == u"\U0001F347" and reel_2 == u"\U0001F347":
        wallet += (wager * 3)
        print("You won $" + str(wager * 3))
    elif reel_1 == u"\U0001F514" and reel_2 == u"\U0001F514" and reel_3 == u"\U0001F514":
        wallet += (wager * 6)
        print("You won $" + str(wager * 6))
    elif reel_1 == u"\U0001F514" and reel_2 == u"\U0001F514":
        wallet += (wager * 5)
        print("You won $" + str(wager * 5))
    elif reel_1 == u"\U0001F525" and reel_2 == u"\U0001F525" and reel_3 == u"\U0001F525":
        wallet += (wager * 100)
        print("You won $" + str(wager * 100))
    else:
        wallet -= wager
        print("No winning combiniation, sorry!")
    playagain()

def playagain():
    global wallet
    print("You currently have $" + str(wallet))
    respin = input("Spin again with the same bet? Y/N? ")
    if respin.lower() == 'y' or respin.lower() == 'yes':
        spin()
    elif respin.lower() == 'n' or respin.lower() == 'no':
        rebet = input("Would you like play again with a different bet? Y/N? ")
        if rebet.lower() == 'y' or respin.lower() == 'yes':
            bet()
        else:
            print("You finished with $" + str(wallet))
            print("See you next time!")

bet()