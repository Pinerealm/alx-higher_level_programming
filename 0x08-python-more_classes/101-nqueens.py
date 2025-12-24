#!/usr/bin/python3
"""Module for solving the N queens puzzle."""
import sys


class NQueens:
    """Represents the N queens puzzle."""

    def __init__(self, n):
        """Initializes the N queens puzzle.

        Args:
            n (int): The size of the board.
        """
        self.n = n
        self.solutions = []

    def solve(self):
        """Solves the N queens puzzle."""
        self._solve([], 0)

    def _solve(self, queens, row):
        """solve method helper.

        Args:
            queens (list): The queens on the board.
            row (int): The current row.
        """
        if row == self.n:
            self.solutions.append(queens)
            return
        for col in range(self.n):
            if self._is_valid(queens, row, col):
                self._solve(queens + [(row, col)], row + 1)

    def _is_valid(self, queens, row, col):
        """Checks if a queen can be placed at a given position.

        Args:
            queens (list): The queens on the board.
            row (int): The row of the queen.
            col (int): The column of the queen.

        Returns:
            True if the queen can be placed, False otherwise.
        """
        for queen in queens:
            if queen[1] == col or queen[0] - queen[1] == row - col or \
                    queen[0] + queen[1] == row + col:
                return False
        return True

    def print_solutions(self):
        """Prints the solutions to the N queens puzzle."""
        for solution in self.solutions:
            print("[", end="")
            for queen in solution:
                print("[{}, {}]".format(queen[0], queen[1]), end="")
                if queen != solution[-1]:
                    print(", ", end="")
            print("]")
        if not self.solutions:
            print("No solution")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        n = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)
    nqueens = NQueens(n)
    nqueens.solve()
    nqueens.print_solutions()
