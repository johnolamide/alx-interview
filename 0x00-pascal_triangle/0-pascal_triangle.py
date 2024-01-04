""" This script defines a pascal triangle creator
"""


def pascal_triangle(n):
    """
        function definition of the pascal triangle
        args:
            n (int): integer for pascal triangle
    """
    if (n <= 0):
        return []

    triangle = [[1]]

    for i in range (1, n):
        row = [1]
        last_row = triangle[-1]
        row += [sum(pair) for pair in zip(last_row, last_row[1:])]
        row.append(1)
        triangle.append(row)

    return triangle
