import os

puzzle = '070000043040009610800634900094052000358460020000800530080070091902100005007040802'

sudoku = []
row = []

for i in range(len(puzzle)):
    row.append(int(puzzle[i]))
    if (i+1) % 9 == 0:
        sudoku.append(row)
        row = []


def solve(board):
    find = is_empty(board)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    boardx_x = pos[1] // 3
    boardx_y = pos[0] // 3

    for i in range(boardx_y*3, boardx_y*3 + 3):
        for j in range(boardx_x * 3, boardx_x*3 + 3):
            if board[i][j] == num and (i,j) != pos:
                return False

    return True


def print_sudoku(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("------+-------+-------")

        for j in range(len(board[0])):
            if j % 3 == 0 and j != 0:
                print("| ", end="")

            if j == 8:
                if board[i][j] == 0:
                    print(" ")
                else:
                    print(board[i][j])
            else:
                if board[i][j] == 0:
                    print(" " + " ", end="")
                else:
                    print(str(board[i][j]) + " ", end="")


def is_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)

    return None

os.system('cls') # For linux or mac, replace 'cls' with 'clear'
print("\nProblem: \n")
print_sudoku(sudoku) # Unsolved

solve(sudoku)
input("\nPress Enter to See the Solution...")

os.system('cls') # For linux or mac, replace 'cls' with 'clear'
print("\nSolution: \n")
print_sudoku(sudoku) # Solved

solution = ''
for i in range(9):
    for j in range(9):
        solution = solution+str(sudoku[i][j])

if solution == '679518243543729618821634957794352186358461729216897534485276391962183475137945862':
    print("\nThe solution is verified")