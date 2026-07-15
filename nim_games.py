initial_matches = 21
min_matches_to_remove = 1
max_matches_to_remove = 4


def ask_players_name():
    """
    Demande le nom des joueurs.
    :return: Liste des joueurs.
    """
    return [
        input("Saisissez le nom du joueur A :  "),
        input("Saisissez le nom du joueur B :  ")
    ]


def ask_who_start(players_list):
    """
    Demande de choisir quel joueur commence la partie.
    :param players_list: Liste des joueurs.
    :return: Chiffre qui sera l'index du joueur dans la liste des joueurs.
    """
    choice = int(input(f"Qui commence? 1-{players_list[0]} ou 2-{players_list[1]}: "))
    return choice - 1


def ask_nbr_matches():
    """
    Demande le nombre d'allumettes à retirer.
    :return: Le nombre d'allumettes.
    """
    while True:
        taken_matches = int(input(f"Combien d'allumettes souhaitez-vous retirer? "
                                  f"(Saisir un chiffre entre {min_matches_to_remove} et {max_matches_to_remove}).) "))
        if taken_matches > max_matches_to_remove:
            print("Vous pouvez retirer 4 allumettes au maximum.")
            continue
        elif taken_matches < min_matches_to_remove:
            print("Vous devez retirer 1 allumette au minimum.")
            continue

        return taken_matches


def play_game(players_list, first_player_index):
    """
    Partie : Tant qu'il reste une ou des allumettes, demande à tour de role de jouer.
    :return: None
    """
    stock_matches = initial_matches
    current_player_index = first_player_index

    while stock_matches > 0:
        current_player = players_list[current_player_index]
        print(f"C'est au tour de {current_player}")

        taken_matches = ask_nbr_matches()
        stock_matches -= taken_matches

        if stock_matches == 0:
            print(f"{current_player} a perdu, il a pris la dernière allumette!")
            return

        current_player_index = 1 - current_player_index
        print(f"Il reste  {stock_matches} allumettes.")


if __name__ == "__main__":
    players = ask_players_name()
    starting_player_index = ask_who_start(players)

    print(f"{players[starting_player_index]} est le premier à jouer!")
    play_game(players, starting_player_index)
