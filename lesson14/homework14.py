#Object oriented RPSLS game

from random import choice


class Player:
    """
Class representing players choice in a game.

Attributes: user_choice --> a string of user input, defined by staticmethod player_input.

    """
    def __init__(self, user_choice):
        self.user_choice = user_choice

    @property
    def user_choice(self):
        return self._user_choice

    @user_choice.setter
    def user_choice(self, user_choice):
        """
        setter method with additional validation.
        """
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        if user_choice not in choices:
            raise ValueError('Invalid value for a figure received')
        self._user_choice = user_choice

    @staticmethod
    def player_input():
        """
        Receives user input and validates it by comparing to acceptable figures.
        Returns:
        A str containing user figure.
        """
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        while True:
            player = input('Rock, paper, scissors, lizard or Spock?: ')
            if player.lower() in choices:
                return player

    def __str__(self):
        return self.user_choice


class GameFigure:
    """
    A class defining figure, chosen by computer to be compared in a game versus user figure.
    Attributes: game_figure
    """
    def __init__(self, game_figure):
        self.game_figure = game_figure

    @staticmethod
    def figure_select():
        """
        Static method used to define computer figure to be compared in a game.
        Returns: str of randomly chosen figure

        """
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        return choice(choices)

    @property
    def game_figure(self):
        return self._game_figure

    @game_figure.setter
    def game_figure(self, game_figure):
        """
        a setter method with validation.
        """
        choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']
        if game_figure not in choices:
            raise ValueError('Invalid value for a figure received')
        self._game_figure = game_figure

    def __str__(self):
        return self.game_figure


class Game:
    """
    Class representing the main action of a game. Contains static method game() of The Game itself.
    """
    def __init__(self, user_choice, ai_decision):
        Player.user_choice = user_choice
        GameFigure.game_figure = ai_decision

    @staticmethod
    def game():
        """
        Static method of a Game itself. Process figures to bring outcome of a battle and record stats to an external txt.
        Returns:
        str containing outcome of a battle
        """
        ai_decision = GameFigure.figure_select()
        user_choice = Player.player_input()
        print(f'You chose {user_choice}.')
        print(f'Computer chose {ai_decision}.')
        rules = {
            'rock': ['scissors', 'lizard'],
            'paper': ['rock', 'spock'],
            'scissors': ['paper', 'lizard'],
            'lizard': ['paper', 'spock'],
            'spock': ['rock', 'scissors']
        }
        if ai_decision in rules.get(user_choice, []):
            message = 'You won. Computer lost.\n'
        elif user_choice in rules.get(ai_decision, []):
            message = 'You lost. Computer won.\n'
        else:
            message = 'Draw\n'
        print(message)
        file = open('stats.txt', 'a')
        file.write(
            f'The game was played. You chose {user_choice}. Computer chose {ai_decision}. {message}\n')
        file.close()
        return message


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
        Game.game()
        yes = ['yes', 'y']
        play_again = input('Type in \'y\' or \'yes\' to play again: ')

        if play_again.lower() not in yes:
            print(thanks)
            return thanks


main()
