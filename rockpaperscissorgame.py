from random import randint
import colorama

from colorama import Fore, Back, Style
colorama.init(autoreset=True)

print(Fore.YELLOW+Back.BLUE+'***************Permainan Batu , Kertas , Gunting***************\n')

#create a list of play options
t = ["Batu", "Kertas", "Gunting"]

#assign a random play to the computer
computer = t[randint(0,2)]

#set player to False
player = False

while player == False:
#set player to True
    player = input("\nBatu , Kertas , Gunting?")
    if player == computer:
        print("\U0001f600")
    elif player == "Batu":
        if computer == "Kertas":
            print("Anda Kalah!", computer, "Bantu", player)
        else:
            print("Anda Menang!", player, "Musnahkan", computer)
    elif player == "Kertas":
        if computer == "Gunting":
            print("Anda Kalah!", computer, "Potong", player)
        else:
            print("Anda Menang!", player, "Bantu", computer)
    elif player == "Gunting":
        if computer == "Batu":
            print("Anda Kalah!", computer, "Musnahkan", player)
        else:
            print("Anda Menang!", player, "potong", computer)

    else:
        print("TIDAK SAH.SEMAK EJAAN!")


    #player was set to True, but we want it to be False so the loop continues
    player = False
    computer = t[randint(0,2)]