from random import *
from time import *
from welcome import game_name
from player_asset import *
from computer_asset import *

# game name :
print(game_name)

# player name :
sleep(1)
player_name = input("ENTER YOUR NAME : ")
print("\n" + "*" * 25)
print("WELCOME", player_name.upper())
print("*" * 25)

# player options :
print('''
CHOICE FOR PLAYERS ARE :
    
1 = Stone
2 = Paper 
3 = Scissor
''')


# main game :
def game():
    loop()


# player choice :
def player_turn():
    a = True
    while (a == True):
        player_choice = int(input("\nEnter your choice : "))
        if player_choice > 0 and player_choice < 4:
            a = False
        else:
            print("!! THE OPTION IS NOT PRESENT !!")
            pass
    if player_choice == 1:
        print("---------- PLAYER TURN ----------")
        P1 = stone_art_player
        print(P1)
    elif player_choice == 2:
        print("---------- PLAYER TURN ----------")
        P2 = paper_art_player
        print(P2)
    elif player_choice == 3:
        print("---------- PLAYER TURN ----------")
        P3 = scissor_art_player
        print(P3)
    return player_choice


# computer choice :
def comp():
    choice_list = [1, 2, 3]
    computer_choice = choice(choice_list)
    if computer_choice == 1:
        print("---------- OPPONENT TURN ----------")
        C1 = stone_art_comp
        print(C1)
    elif computer_choice == 2:
        print("---------- OPPONENT TURN ----------")
        C2 = paper_art_comp
        print(C2)
    elif computer_choice == 3:
        print("---------- OPPONENT TURN ----------")
        C3 = scissor_art_comp
        print(C3)
    return computer_choice
    print(computer_choice)


# game loop :
def loop():
    player_score = 0
    computer_score = 0
    chances = 0
    while not (chances == 5):
        sleep(1)
        print("_" * 100)
        sleep(1)
        player = player_turn()
        computer = comp()
        if player == computer:
            sleep(1)
            print("\n!!! DRAW, NO POINTS FOR ANYONE !!!\n")
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            pass
        elif player == 1 and computer == 2:
            sleep(1)
            print("\n!!! PAPER WINS, COMPUTER GAINS POINT !!!\n")
            computer_score += 1
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            chances += 1
        elif player == 2 and computer == 3:
            sleep(1)
            print("\n!!! SCISSOR WINS, COMPUTER GAINS POINT !!!\n")
            computer_score += 1
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            chances += 1
        elif player == 3 and computer == 1:
            sleep(1)
            print("\n!!! STONE WINS, COMPUTER GAINS POINT !!!\n")
            computer_score += 1
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            chances += 1
        elif player == 2 and computer == 1:
            sleep(1)
            print("\n!!! PAPER WINS,", player_name.upper(),
                  "GAINS POINT !!!\n")
            player_score += 1
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            chances += 1
        elif player == 3 and computer == 2:
            sleep(1)
            print("\n!!! SCISSOR WINS,", player_name.upper(),
                  "GAINS POINT !!!\n")
            player_score += 1
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            chances += 1
        elif player == 1 and computer == 3:
            sleep(1)
            print("\n!!! STONE WINS,", player_name.upper(),
                  "GAINS POINT !!!\n")
            player_score += 1
            print("PLAYER SCORE = ", player_score)
            print("OPPONENT SCORE = ", computer_score)
            chances += 1
    print("_" * 100, "\n")
    if player_score > computer_score:
        print("THE FINAL SCORE OF PLAYER IS ", player_score)
        print("THE FINAL SCORE OF OPPONENT IS ", computer_score)
        print("\n\n")
        print("*" * 50, "\n")
        print(player_name.upper(), "WINS THE GAME\n")
        print("*" * 50)
    elif player_score < computer_score:
        print("THE FINAL SCORE OF PLAYER IS ", player_score)
        print("THE FINAL SCORE OF OPPONENT IS ", computer_score)
        print("\n\n")
        print("*" * 50, "\n")
        print("OPPONENT WINS THE GAME\n")
        print("*" * 50)
    elif player_score == computer_score:
        print("THE FINAL SCORE OF PLAYER IS ", player_score)
        print("THE FINAL SCORE OF OPPONENT IS ", computer_score)
        print("\n\n")
        print("*" * 50, "\n")
        print("THE GAME IS DRAW, NO ONE WON\n")
        print("*" * 50)


game()
