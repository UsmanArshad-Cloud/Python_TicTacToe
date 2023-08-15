import string


class Helper:
    @staticmethod
    def initialize_board(n):
        matrix = []
        letters = string.ascii_lowercase
        index = 0
        for i in range(n):
            row = []
            for j in range(n):
                row.append(letters[index % len(letters)])
                index += 1
            matrix.append(row)
        return matrix

    @staticmethod
    def print_board(matrix, n):
        for i in range(n):
            for j in range(n):
                print(f" {matrix[i][j]} |", end="")
            print("")
            print("____" * n)

    @staticmethod
    def update_matrix(matrix, n, letter, symbol):
        for i in range(n):
            for j in range(n):
                if matrix[i][j] == letter and matrix[i][j] != "X" and matrix[i][j] != "O":
                    matrix[i][j] = symbol
                    return True
        print("Your input does not match the content of Matrix")
        return False

    @staticmethod
    def check_win(n, word, board):
        word_count_diagonal = 0
        word_count_anti_diagonal = 0
        is_found = False
        for i in range(n):
            word_count_x = 0  # Variable Initialization
            word_count_y = 0
            if board[i][n - 1] == word:
                word_count_anti_diagonal += 1  # Checking for the Anti-Diagonal
            for j in range(n):
                if i == j:
                    if board[i][j] == word:  # Checking for the Main Diagonals
                        word_count_diagonal += 1
                if board[i][j] == word:
                    word_count_x += 1  # Checking Row Wise Neighbours Of Each Element
                if board[j][i] == word:
                    word_count_y += 1  # Checking Column Wise Neighbours of Each Element
            is_found = True if word_count_x == n or word_count_y == n else False
        return True if word_count_diagonal == n or word_count_anti_diagonal == n or is_found else False
