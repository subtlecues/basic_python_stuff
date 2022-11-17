###    Напишіть гру "rock scissors paper lizard spock". Використайте розділення всієї програми на функції (Single-Responsibility principle). Як скелет-заготовку можна використати приклад з заняття.
# До кожної функції напишіть докстрінг або анотацію

### The game is in English language and receives English only input.

from random import choice


def receive_user_input():
    """
    A simple function which takes user input to be processed during game. Written with a while loop to exclude wrong
    inputs.
    Returns:
    str containing user choice
    """
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    while True:
        player = input('Rock, paper, scissors, lizard or Spock?: ')
        if player.lower() in choices:
            return player


def ai_choice():
    """
    Automated func which chooses a computers game-gesture using choice method.
    Returns:
    str computer choice.
    """
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    ai = choice(choices)
    return ai


def game_outcome():
    """
    The game function. Compares computer and user choices by iterating through a dict containing game rules.
    Returns:
    a str containing game outcome.
    """
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
    ai_decision = ai_choice()
    user_choice = receive_user_input()
    print(f'You chose {user_choice.lower()}.')
    print(f'Computer chose {ai_decision}.')
    games = {'win': [(choices[0], choices[2]),
                     (choices[0], choices[3]),
                     (choices[1], choices[0]),
                     (choices[1], choices[4]),
                     (choices[2], choices[1]),
                     (choices[2], choices[3]),
                     (choices[3], choices[1]),
                     (choices[3], choices[4]),
                     (choices[4], choices[0]),
                     (choices[4], choices[2]),
                     ],

             'lose': [(choices[0], choices[1]),
                      (choices[0], choices[4]),
                      (choices[1], choices[2]),
                      (choices[1], choices[3]),
                      (choices[2], choices[0]),
                      (choices[2], choices[4]),
                      (choices[3], choices[2]),
                      (choices[3], choices[0]),
                      (choices[4], choices[3]),
                      (choices[4], choices[1]),
                      ],

             'tie': [(choices[0], choices[0]),
                     (choices[1], choices[1]),
                     (choices[2], choices[2]),
                     (choices[3], choices[3]),
                     (choices[4], choices[4]),
                     ]}
    for outcome in games:
        if (user_choice.lower(), ai_decision) in games[outcome]:
            outcome = f'You {outcome} against your opponent!\n'
            return outcome


def main():
    """
    This function is used to print user greeting, execute the game process, print the game outcome and to ask if the
    user wants to play game again. Finishes the game  with a thanking message if user refuses to play again.
    Returns:
    str containing 'Thanks for playing!' message.
    """
    print('The computer challenges you to play \"Rock, paper, scissors, lizard, Spock\"!\n')
    thanks = 'Thanks for playing!'
    while True:
        print(game_outcome())
        yes = ['yes', 'y']
        play_again = input('Type in \'y\' or \'yes\' to play again: ')

        if play_again.lower() not in yes:
            print(thanks)
            return thanks


main()
