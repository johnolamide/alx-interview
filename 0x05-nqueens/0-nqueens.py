#!/usr/bin/python3
""" This Script contains the function definition of nqueens
"""
import sys


def solve_n_queens(n):
    def can_place(pos, ocuppied_positions):
        for i in range(len(ocuppied_positions)):
            if ocuppied_positions[i] == pos or \
                ocuppied_positions[i] - i == pos - len(ocuppied_positions) or \
               ocuppied_positions[i] + i == pos + len(ocuppied_positions):
                return False
        return True

    def place_queen(n, index, ocuppied_positions):
        if index == n:
            return [ocuppied_positions]
        else:
            result = []
            for pos in range(n):
                if can_place(pos, ocuppied_positions):
                    sumt = ocuppied_positions + [pos]
                    result += place_queen(n, index + 1, sumt)
            return result

    return place_queen(n, 0, [])


def main():
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

    solutions = solve_n_queens(n)
    for solution in solutions:
        formatted_solution = [[i, pos] for i, pos in enumerate(solution)]
        print(formatted_solution)


if __name__ == "__main__":
    main()
