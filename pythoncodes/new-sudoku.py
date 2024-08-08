import random
from rich.console import Console
from rich.table import Table
from rich.prompt import Prompt
from rich.panel import Panel

console = Console()

def print_board(board):
    table = Table(show_header=True, header_style="bold magenta")
    for i in range(9):
        table.add_column(f"Col {i+1}", justify="center")
    
    for row in board:
        table.add_row(*[str(num) if num != 0 else ' ' for num in row])

    console.print(table)

def is_valid(board, row, col, num):
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False

    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False
    return True

def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):
                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True

def create_sudoku_board():
    board = [[0] * 9 for _ in range(9)]
    for i in range(9):
        row, col = random.randint(0, 8), random.randint(0, 8)
        num = random.randint(1, 9)
        while not is_valid(board, row, col, num) or board[row][col] != 0:
            row, col = random.randint(0, 8), random.randint(0, 8)
            num = random.randint(1, 9)
        board[row][col] = num

    solve_sudoku(board)
    
    for _ in range(random.randint(40, 50)):
        row, col = random.randint(0, 8), random.randint(0, 8)
        board[row][col] = 0
    
    return board

def main():
    console.print(Panel("Sudoku Generator and Solver", style="bold blue"))
    mode = Prompt.ask("Choose mode: [1] Generate New Sudoku, [2] Solve Existing Sudoku", choices=["1", "2"], default="1")

    if mode == "1":
        board = create_sudoku_board()
        console.print(Panel("Generated Sudoku Board", style="cyan"))
        print_board(board)
    else:
        board = []
        console.print(Panel("Enter the Sudoku board row by row, use 0 for empty cells.", style="cyan"))
        for i in range(9):
            row = list(map(int, Prompt.ask(f"Row {i+1}").split()))
            board.append(row)
    
    if solve_sudoku(board):
        console.print(Panel("Solved Sudoku Board", style="green"))
        print_board(board)
    else:
        console.print(Panel("No solution exists for the given Sudoku.", style="red"))

if __name__ == "__main__":
    main()
