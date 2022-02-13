# Tic Tac Toe Game

import random
from os import system, name


class Board():
    def __init__(self):
        # Define board as dictionary
        self.cells = {'1': ' ', '2': ' ', '3': ' ',
                      '4': ' ', '5': ' ', '6': ' ',
                      '7': ' ', '8': ' ', '9': ' '}

    def display(self):

        #
        # Display the board
        print(self.cells['1'] + '|' + self.cells['2'] + '|' + self.cells['3'])
        print("-+-+-")
        print(self.cells['4'] + '|' + self.cells['5'] + '|' + self.cells['6'])
        print("-+-+-")
        print(self.cells['7'] + '|' + self.cells['8'] + '|' + self.cells['9'])
        return

    def update_board(self, move, player):

        # Update the board with a players move
        self.cells[move] = player
        self.display()

    def is_empty(self, move):
        if self.cells[move] == ' ':
            return True
        else:
            print("Position already taken, try another one!")
            return False

    def check_winner(self):
        # Check if winning condition is fulfilled and determine the winner.
        if self.cells['1'] == self.cells['2'] == self.cells['3'] != ' ':
            self.winner = self.cells['1']
            return True
        elif self.cells['4'] == self.cells['5'] == self.cells['6'] != ' ':
            self.winner = self.cells['4']
            return True
        elif self.cells['7'] == self.cells['8'] == self.cells['9'] != ' ':
            self.winner = self.cells['7']
            return True
        elif self.cells['1'] == self.cells['4'] == self.cells['7'] != ' ':
            self.winner = self.cells['1']
            return True
        elif self.cells['2'] == self.cells['5'] == self.cells['8'] != ' ':
            self.winner = self.cells['2']
            return True
        elif self.cells['3'] == self.cells['6'] == self.cells['9'] != ' ':
            self.winner = self.cells['3']
            return True
        elif self.cells['1'] == self.cells['5'] == self.cells['9'] != ' ':
            self.winner = self.cells['1']
            return True
        elif self.cells['3'] == self.cells['5'] == self.cells['7'] != ' ':
            self.winner = self.cells['3']
            return True

    def check_tie(self):
        # Check if all all cells are full and we have a tie.
        if ' ' in self.cells.values():
            return False
        else:
            print("We have a tie!")
            return True

    def get_empty_cells(self):
        self.empty_cells = []
        for key, value in self.cells.items():
            if ' ' == value:
                self.empty_cells.append(key)
        return

    def clear_screen(self):
        # for Windows
        if name == 'nt':
            _ = system('cls')
        # for Mac and Linux (os name is 'posix')
        else:
            _ = system('clear')


class Player():
    def __init__(self):
        # Set players to O and X
        self.players = ['O', 'X']
        # Make random selection of player symbols
        self.human = random.choice(self.players)
        if self.human == 'X':
            self.computer = 'O'
        else:
            self.computer = 'X'
        return

    def computer_move(self):
        # Simple AI for computer moves
        board.get_empty_cells()
        self.cells_copy = board.cells.copy()
        self.empty = board.empty_cells
        # Check if move on empty position can win
        for self.move in self.empty:
            self.cells_copy = board.cells.copy()
            board.cells[self.move] = player.computer
            if board.check_winner():
                # Undo Changes if move wins
                board.cells = self.cells_copy.copy()
                return self.move
            board.cells = self.cells_copy.copy()

        # Check if human can win with next move an block it
        for self.move in self.empty:
            self.cells_copy = board.cells.copy()
            board.cells[self.move] = player.human
            if board.check_winner():
                # If move wins undo changes to game
                board.cells = self.cells_copy.copy()
                return self.move
            # Undo changes to game
            board.cells = self.cells_copy.copy()

        # Move to centre if possible
        if '5' in self.empty:
            return '5'

        # Try to move to a corner
        choices = ['1', '3', '7', '9']
        # shuffle to make game interesting
        random.shuffle(choices)
        for self.move in choices:
            if self.move in self.empty:
                return self.move

        # Try to move to one side
        choices = ['2', '4', '6', '8']
        # shuffle to make game interesting
        random.shuffle(choices)
        for self.move in choices:
            if self.move in self.empty:
                return self.move
        return self.move


def game(move, playing):
    board.clear_screen()
    board.update_board(move, playing)
    is_won = board.check_winner()
    board_full = board.check_tie()
    if is_won:
        print(f"The winner is {board.winner}")
        return False
    if board_full:
        return False


if __name__ == "__main__":
    # Run game until y/n
    play_forever = True
    while play_forever:

        # Start game and display board
        board = Board()
        board.clear_screen()
        print("Welcome to Tic Tac Toe")
        board.display()
        # Set random player human and computer
        player = Player()
        print(f"You are player: {player.human}")
        # Want to play game forever?

        # Run game as long condition is true
        run_game = True
        while run_game:
            # Get user input and check if move is valid
            check_user = True
            while check_user:
                user_move = input(f"Player {player.human} enter your move (1-9): ")
                print('\n')
                if board.is_empty(user_move):
                    check_user = False
                else:
                    check_user = True

            # Update board with user move
            human = game(user_move, player.human)
            if human is False:
                run_game = False
                break

            # Update board with computer move
            c_move = player.computer_move()
            computer = game(c_move, player.computer)
            if computer is False:
                run_game = False
                break
        play_again = input("Play another game? (y/n)")
        if play_again == "n":
            play_forever = False
        else:
            continue
