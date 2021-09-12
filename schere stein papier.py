import random


while True:
    player_me = input("Schere, Stein, Papier: ")
    player_me = player_me.lower()
    player_enemie = random.randint(1, 3)
    if player_me == "schere":
        if player_enemie == 1:
            print("Gegner hat Schere: Unentschieden!")
            break
        elif player_enemie == 2:
            print("Gegner hat Stein: Verloren!")
            break
        else:
            print("Gegner hat Papier: Gewonnen!")
            break
    elif player_me == "stein":
        if player_enemie == 1:
            print("Gegner hat Schere: Gewonnen!")
            break
        elif player_enemie == 2:
            print("Gegner hat Stein: Unentschieden!")
            break
        else:
            print("Gegner hat Papier: Verloren!")
            break
    elif player_me == "papier":
        if player_enemie == 1:
            print("Gegner hat Schere: Verloren!")
            break
        elif player_enemie == 2:
            print("Gegner hat Stein: Gewonnen!")
            break
        else:
            print("Gegner hat Papier: Unentschieden!")
            break
    else:
        print("Falsche eingabe!")
        continue
