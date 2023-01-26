import random

choice = {'': '', 'Foot': 'Cockroach', 'Nuke': 'Foot', 'Cockroach': 'Nuke'}


def game(player, ai, win, tie):
    for key in choice:
        if player == key and ai == choice[key]:
            print('You WIN!')
            win += 1
            return (win, tie)
    else:
        if player == ai:
            if player == 'nuke':
                print('Both LOSE!')
            print('It is a tie!')
            tie += 1
            return (win, tie)
        else:
            print('You LOSE!')

    return (win, tie)


def main():

    round = 0
    win = 0
    tie = 0

    while True:
        player = input('Foot, Nuke or Cockroach? (Quit ends): ').capitalize()
        choice_keys = list(choice.keys())
        ai = choice_keys[random.randint(1, 3)]

        if player == 'Quit':
            print(
                f'You played {round} rounds, and won {win} rounds, playing tie in {tie} rounds.')
            break

        if player not in choice_keys:
            print('Incorrect selection.')
            continue

        print(f'You chose: {player}\nComputer chose: {ai}')

        round += 1
        (win, tie) = game(player, ai, win, tie)


if __name__ == '__main__':
    main()
