def solve_n_queens(n):
    def is_safe(board, row, col):
        # Check vertical (column) safety
        for i in range(row):
            if board[i][col] == 1:
                return False
        # Check diagonal safety
        for i in range(row):
            # Find the column where the queen is placed in row i.
            for j in range(n):
                if board[i][j] == 1 and abs(row - i) == abs(col - j):
                    return False
        return True

    def solve_n_queens_util(board, row):
        # Base case: all queens are placed
        if row == n:
            return True
        # Try placing a queen in each column of the current row
        for col in range(n):
            if is_safe(board, row, col):
                board[row][col] = 1
                if solve_n_queens_util(board, row + 1):
                    return True
                # Backtrack
                board[row][col] = 0
        return False

    board = [[0] * n for _ in range(n)]
    if not solve_n_queens_util(board, 0):
        print("Solution does not exist")
        return False
    print("One solution:")
    for row in board:
        print(*row)
    return True

solve_n_queens(5)

