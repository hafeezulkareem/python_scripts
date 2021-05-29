import random


class TicTacToe:

    # initialising the Tic Tac Toe board
    def __init__(self):

        self.board = []
        self.winner = None

        for i in range(3):
            self.board.append([' ', ' ', ' '])

    def add_user_position(self, i, j):

        if self.is_empty(i, j):
            self.board[i][j] = "X"
            self.show_board()
            if self.is_game_over():
                print("X won the match")
            else:
                if self.is_board_full() and self.winner is None:
                    print("Draw")
                else:
                    self.add_computer_position()
        else:
            print(f"Position {i} {j} is filled already.")
            i, j = map(int, input("Enter position again: ").split(" "))
            self.add_user_position(i, j)

    def add_computer_position(self):

        i, j = random.randint(0, 2), random.randint(0, 2)

        while not self.is_empty(i, j):
            i, j = random.randint(0, 2), random.randint(0, 2)
        self.board[i][j] = "O"

        self.show_board()
        if self.is_game_over():
            print("O won the match")
        else:
            if self.is_board_full() and self.winner is None:
                print("Draw")
            else:
                i, j = map(int, input("Enter position: ").split(" "))
                self.add_user_position(i, j)

    def is_empty(self, i, j):
        if self.board[i][j] == ' ':
            return True
        else:
            return False

    def is_game_over(self):
        winning_cases = [["00", "01", "02"], ["10", "11", "12"], ["20", "21", "22"], ["00", "10", "20"],
                         ["01", "11", "21"],
                         ["02", "12", "22"], ["00", "11", "22"], ["02", "11", "20"]]

        for winning_case in winning_cases:

            is_true = [True if not self.is_empty(int(case[0]), int(case[1])) else False for case in winning_case]

            if all(is_true):
                is_user = [True if self.board[int(case[0])][int(case[1])] == "X" else False for case in winning_case]
                if is_user and all(is_user):
                    self.winner = "X"
                    return True

                is_computer = [True if self.board[int(case[0])][int(case[1])] == "O" else False for case in
                               winning_case]
                if is_computer and all(is_computer):
                    self.winner = "O"
                    return True

        return False

    def is_board_full(self):
        for i in range(3):
            for j in range(3):
                if self.is_empty(i, j):
                    return False
        return True

    def show_board(self):
        for i in range(len(self.board)):
            for j in range(len(self.board)):
                print(self.board[i][j], end="|" if j is not 2 else " ")
            if i is not 2:
                print("\n-+-+-")
        print("\n-----------------------------\n")


def main():
    tic_tac_toe = TicTacToe()
    i, j = map(int, input("Enter position: ").split(" "))
    tic_tac_toe.add_user_position(i, j)


if __name__ == "__main__":
    main()
