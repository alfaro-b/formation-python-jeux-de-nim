initial_matches = 21
min_matches_to_remove = 1
max_matches_to_remove = 4


def ask_players_name():
    players = [
        input("Saisissez le nom du joueur A :  "),
        input("Saisissez le nom du joueur B :  ")
    ]
    return players


def ask_who_start(players):
    choice = int(input(f"Qui commence? 1-{players[0]} ou 2-{players[1]}: "))
    return choice - 1


def ask_nbr_matches():
    while True:
        taken_matches = int(input(f"Combien d'allumettes souhaitez-vous retirer? "
                                  f"(Saisir un chiffre entre {min_matches_to_remove} et {max_matches_to_remove}).) "))
        if taken_matches > max_matches_to_remove:
            print("Vous pouvez retirez 4 allumettes au maximum.")
            continue
        elif taken_matches < min_matches_to_remove:
            print("Vous devez retirez 1 allumette au minimum.")
            continue

        return taken_matches


def play_game():
    stock_matches = initial_matches
    current_player_index = starting_player_index

    while stock_matches > 0:
        current_player = players[current_player_index]
        print(f"C'est au tour de {current_player}")

        taken_matches = ask_nbr_matches()
        stock_matches -= taken_matches
        current_player_index = 1 - current_player_index
        print(f"Il reste  {stock_matches} allumettes.")
    print(f"{current_player} a perdu, il a pris la dernière allumette!")


if __name__ == "__main__":
    players = ask_players_name()
    starting_player_index = ask_who_start(players)

    print(f"{players[starting_player_index]} est le premier à jouer!")
    play_game()
