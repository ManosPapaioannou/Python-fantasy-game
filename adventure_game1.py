import time
import random
items = []


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)


def heads_tails():
    coin = ('heads', 'tails')
    while True:
        flip = random.choice(coin)
        your_choice = input('Type heads or tails \n')
        if your_choice == flip:
            print_pause('The coin landed on {} '.format(flip))
            print_pause('Yes, you are victorious!')
            print_pause(' The demon flees in terror\n'
                        ' and you claim the castle!')
            play_again()
        elif your_choice != flip:
            print_pause("Uh oh. Coin landed on {}. The demon laughs at "
                        "you".format(flip))


def intro():
    print_pause("You find yourself outside an old village.\n")
    print_pause("You go towards the village square"
                " and get stopped by an old man\n")
    name = input("What is your name stranger?\n")
    time.sleep(1)
    print_pause("Welcome "+name+"! We have been expecting you.\n ")
    where_to()


def tavern():
    if "coin" in items:
        print_pause("The waitress greets you"
                    " but you don't have enough money..\n")
        where_to()
    else:
        print_pause("The old man leads you to the tavern."
                    "Where after a night of heavy drinking \n"
                    "you wake up in the street with"
                    " only a coin in your pocket"
                    " a coin you remember "
                    "that the old man gave you\n ")
        items.append("coin")
        where_to()


def castle():
    print_pause("The castle lays upon the hill to the north.\n")
    print_pause("You reach the castle's yard and see the demon by a table\n")
    if "coin" in items:
        print_pause("The demon asks you to play a game of heads or tails.\n")
        print_pause("You remember the coin the old man gave you and "
                    " reach in your pocket for it\n")
        heads_tails()
    else:
        print_pause("You get scared by the demon and head"
                    " to the village to consult with the old man\n ")
        tavern()


def where_to():
    while True:
        responce = input("Would you like to visit the tavern\n"
                         "or try to retake the castle from the demon?\n"
                         "type tavern or castle\n").lower()
        if 'tavern' in responce:
            tavern()
        elif 'castle' in responce:
            castle()
        else:
            print_pause("Sorry I didn't understand.\n")


def play_game():
    intro()
    where_to()


def play_again():
    while True:
        print_pause("GAME OVER..")
        decision = input("Would you like to play again? (y/n)")
        if 'y' in decision:
            play_game()
        elif 'n' in decision:
            print_pause("GAME OVER..Good bye!")
            exit()

play_game()
play_again()
