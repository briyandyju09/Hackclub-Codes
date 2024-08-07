import random

class Sudoku:
    def __init__(self):
        self.grid = [[0]*9 for _ in range(9)]
        self.generate_puzzle()
        self.display_grid()
        print("\nSolving the puzzle...\n")
        if self.solve():
            self.display_grid()
        else:
            print("No solution exists.")

    def generate_puzzle(self):
        self.fill_grid()
        self.remove_numbers()
    
    def fill_grid(self):
        self.solve()

    def display_grid(self):
        print("Sudoku Puzzle:")
        for i in range(9):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            row = " | ".join(" ".join(str(self.grid[i][j]) if self.grid[i][j] != 0 else '.' for j in range(9)))
            print(row)
        print()

    def solve(self):
        empty = self.find_empty()
        if not empty:
            return True
        row, col = empty
        for num in range(1, 10):
            if self.is_valid(num, row, col):
                self.grid[row][col] = num
                if self.solve():
                    return True
                self.grid[row][col] = 0
        return False

    def find_empty(self):
        for i in range(9):
            for j in range(9):
                if self.grid[i][j] == 0:
                    return (i, j)
        return None

    def is_valid(self, num, row, col):
        for i in range(9):
            if self.grid[row][i] == num or self.grid[i][col] == num:
                return False
        box_x, box_y = 3 * (row // 3), 3 * (col // 3)
        for i in range(box_x, box_x + 3):
            for j in range(box_y, box_y + 3):
                if self.grid[i][j] == num:
                    return False
        return True

    def remove_numbers(self):
        number_of_cells_to_remove = random.randint(40, 60)
        count = 0
        while count < number_of_cells_to_remove:
            row = random.randint(0, 8)
            col = random.randint(0, 8)
            if self.grid[row][col] != 0:
                backup = self.grid[row][col]
                self.grid[row][col] = 0
                copy_grid = [row[:] for row in self.grid]
                if not self.solve():
                    self.grid[row][col] = backup
                else:
                    count += 1

    def print_solution(self):
        print("Solved Sudoku Puzzle:")
        self.display_grid()

if __name__ == "__main__":
    Sudoku()
