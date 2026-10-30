#!/usr/bin/python3
"""
Solves the N queens puzzle.
"""

import sys


def solve_nqueens(n):
    """Backtracking algorithm to find all solutions for N queens."""
    solutions = []
    board = [-1] * n

    def is_safe(row, col):
        """Check if a queen can be placed at board[row] = col."""
        for r in range(row):
            c = board[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def backtrack(row):
        """Recursive backtracking function to place queens row by row."""
        if row == n:
            sol = [[r, board[r]] for r in range(n)]
            solutions.append(sol)
            return

        for col in range(n):
            if is_safe(row, col):
                board[row] = col
                backtrack(row + 1)
                board[row] = -1

    backtrack(0)
    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    solutions = solve_nqueens(N)
    for solution in solutions:
        print(solution)
