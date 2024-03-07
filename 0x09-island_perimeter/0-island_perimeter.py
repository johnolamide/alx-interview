#!/usr/bin/python3
""" this scripts contains the function island_perimeter """


def island_perimeter(grid):
    """ Calculates the perimeter of the island described in the grid
        Args:
            grid (List[List[int]]): A rectangular grid where
                - 0 represents water
                - 1 represents land

        Returns:
            int: The perimeter of the island
    """
    rows, cols = len(grid), len(grid[0])
    perimeter = 0

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                neighbors = [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]
                for nr, nc in neighbors:
                    if 0 <= nr < rows and 0 <= nc < cols:
                        if grid[nr][nc] == 0:
                            perimeter += 1
                    else:
                        perimeter += 1

    return perimeter
