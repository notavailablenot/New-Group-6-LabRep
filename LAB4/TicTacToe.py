import random

class TicTacToe:
    def __init__(self):
        self.board = []

    def create_board(self):
        for i in range(3):
            row = []
            for j in range(3):
                row.append('-')
            self.board.append(row)

    def get_random_first_player(self):
        return random.randint(0, 1)

    def place_marker(self, row_index, col_index, player):
        self.board[row_index][col_index] = player

    def check_win(self, player):
        n = len(self.board)

        # Check rows and columns for a win
        for i in range(n):
            if all(self.board[i][j] == player for j in range(n)) or \
               all(self.board[j][i] == player for j in range(n)):
                return True

        # Check diagonals for a win
        if all(self.board[i][i] == player for i in range(n)) or \
           all(self.board[i][n - 1 - i] == player for i in range(n)):
            return True

        return False

    def check_draw(self):
        for row in self.board:
            if '-' in row:
                return False
        return True

    def switch_player(self, current_player):
        return 'X' if current_player == 'O' else 'O'

    def display_board(self):
        for row in self.board:
            for marker in row:
                print(marker, end=" ")
            print()

    def start(self):
        self.create_board()
        current_player = 'X' if self.get_random_first_player() == 1 else 'O'

        while True:
            print(f"Player {current_player} turn")
            self.display_board()

            # Take user input for row and column
            row_index, col_index = map(int, input("Enter row and column numbers to place your marker: ").split())

            print()
            # Place the marker on the board
            self.place_marker(row_index - 1, col_index - 1, current_player)

            # Check if the current player has won
            if self.check_win(current_player):
                print(f"Player {current_player} wins the game!")
                break

            # Check if the game is a draw
            if self.check_draw():
                print("Match Draw!")
                break

            # Switch player for the next turn
            current_player = self.switch_player(current_player)

            # Display the updated board
            print()
            self.display_board()

# Start the game
tic_tac_toe = TicTacToe()
tic_tac_toe.start()